"""
OTP Verification Endpoints
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.schemas.otp import OTPVerify, OTPResponse, OTPRequest
from app.services.otp_service import OTPService
from app.services.email_service import EmailService
from app.services.sms_service import SMSService
from app.services.auth import AuthService
from app.models.otp import OTPType


router = APIRouter()


@router.post(
    "/verify-otp",
    response_model=OTPResponse,
    summary="Verify OTP code",
    description="Verify OTP code for email or mobile verification"
)
def verify_otp(
    otp_data: OTPVerify,
    db: Session = Depends(get_db)
):
    """
    Verify OTP code for email or mobile.

    Args:
        otp_data: OTP verification data (email/mobile + code)
        db: Database session

    Returns:
        OTPResponse: Verification result

    Raises:
        HTTPException 400: If OTP is invalid or expired
        HTTPException 404: If user not found
    """
    # Determine OTP type and get user
    user = None
    otp_type = None

    if otp_data.email:
        user = AuthService.get_user_by_email(db, otp_data.email)
        otp_type = OTPType.EMAIL
    elif otp_data.mobile:
        user = AuthService.get_user_by_mobile(db, otp_data.mobile)
        otp_type = OTPType.MOBILE
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Either email or mobile must be provided"
        )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    # Verify OTP
    is_valid = OTPService.verify_otp(
        db=db,
        user_id=user.id,
        otp_type=otp_type,
        code=otp_data.otp_code
    )

    if not is_valid:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid or expired OTP code"
        )

    # Check if user has verified both email and mobile (if mobile provided)
    verification_complete = user.email_verified
    if user.mobile:
        verification_complete = user.email_verified and user.mobile_verified

    message = f"{'Email' if otp_type == OTPType.EMAIL else 'Mobile'} verified successfully"
    if verification_complete:
        message += ". Your account is now fully verified!"
        # Send welcome email
        if otp_type == OTPType.EMAIL:
            EmailService.send_welcome_email(user.email, user.full_name or user.username)
        if user.mobile and user.mobile_verified:
            SMSService.send_welcome_sms(user.mobile, user.full_name or user.username)

    return OTPResponse(
        success=True,
        message=message,
        otp_sent_to=None,
        expires_in_minutes=None
    )


@router.post(
    "/resend-otp",
    response_model=OTPResponse,
    summary="Resend OTP code",
    description="Resend OTP code to email or mobile"
)
def resend_otp(
    otp_request: OTPRequest,
    db: Session = Depends(get_db)
):
    """
    Resend OTP code to email or mobile.

    Args:
        otp_request: OTP resend request (email or mobile)
        db: Database session

    Returns:
        OTPResponse: OTP sent confirmation

    Raises:
        HTTPException 404: If user not found
        HTTPException 400: If user already verified
    """
    # Determine OTP type and get user
    user = None
    otp_type = None
    recipient = None

    if otp_request.email:
        user = AuthService.get_user_by_email(db, otp_request.email)
        otp_type = OTPType.EMAIL
        recipient = otp_request.email

        if user and user.email_verified:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already verified"
            )

    elif otp_request.mobile:
        user = AuthService.get_user_by_mobile(db, otp_request.mobile)
        otp_type = OTPType.MOBILE
        recipient = otp_request.mobile

        if user and user.mobile_verified:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Mobile already verified"
            )
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Either email or mobile must be provided"
        )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    # Create new OTP
    otp = OTPService.create_otp(
        db=db,
        user_id=user.id,
        otp_type=otp_type,
        recipient=recipient
    )

    # Send OTP
    sent_successfully = False
    if otp_type == OTPType.EMAIL:
        sent_successfully = EmailService.send_otp_email(
            to_email=recipient,
            otp_code=otp.code,
            user_name=user.full_name
        )
    elif otp_type == OTPType.MOBILE:
        sent_successfully = SMSService.send_otp_sms(
            to_mobile=recipient,
            otp_code=otp.code,
            user_name=user.full_name
        )

    if not sent_successfully:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to send OTP. Please try again."
        )

    return OTPResponse(
        success=True,
        message=f"OTP sent successfully to {'email' if otp_type == OTPType.EMAIL else 'mobile'}",
        otp_sent_to=recipient,
        expires_in_minutes=5
    )
