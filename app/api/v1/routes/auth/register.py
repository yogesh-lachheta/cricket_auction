"""
User Registration Endpoint
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.schemas.user import UserCreate, UserResponse
from app.schemas.otp import OTPResponse
from app.services.auth import AuthService
from app.services.otp_service import OTPService
from app.services.email_service import EmailService
from app.services.sms_service import SMSService
from app.models.otp import OTPType


router = APIRouter()


@router.post(
    "/register",
    response_model=dict,
    status_code=status.HTTP_201_CREATED,
    summary="Register a new user with OTP verification",
    description="Create a new user account and send OTP for email/mobile verification"
)
def register_user(
    user_data: UserCreate,
    db: Session = Depends(get_db)
):
    """
    Register a new user account with OTP verification.

    Flow:
    1. Create user account (unverified)
    2. Send OTP to email
    3. Send OTP to mobile (if provided)
    4. User must verify OTP to activate account

    Args:
        user_data: User registration data (email, username, password, mobile, etc.)
        db: Database session

    Returns:
        dict: Registration success message with OTP sent info

    Raises:
        HTTPException 400: If email, username, or mobile already exists
    """
    # Create user (OAuth users don't need OTP)
    send_otp = user_data.oauth_provider is None
    user = AuthService.create_user(db, user_data, send_otp=send_otp)

    # For OAuth users, skip OTP and return user directly
    if user_data.oauth_provider:
        return {
            "success": True,
            "message": f"Account created successfully via {user_data.oauth_provider}",
            "user": UserResponse.model_validate(user),
            "requires_verification": False
        }

    # Send OTP to email
    email_otp = OTPService.create_otp(
        db=db,
        user_id=user.id,
        otp_type=OTPType.EMAIL,
        recipient=user.email
    )

    email_sent = EmailService.send_otp_email(
        to_email=user.email,
        otp_code=email_otp.code,
        user_name=user.full_name
    )

    # Send OTP to mobile (if provided)
    mobile_sent = False
    if user.mobile:
        mobile_otp = OTPService.create_otp(
            db=db,
            user_id=user.id,
            otp_type=OTPType.MOBILE,
            recipient=user.mobile
        )

        mobile_sent = SMSService.send_otp_sms(
            to_mobile=user.mobile,
            otp_code=mobile_otp.code,
            user_name=user.full_name
        )

    # Prepare response
    otp_sent_to = []
    if email_sent:
        otp_sent_to.append(f"email ({user.email})")
    if mobile_sent:
        otp_sent_to.append(f"mobile ({user.mobile})")

    return {
        "success": True,
        "message": "Account created successfully. Please verify your OTP.",
        "user_id": user.id,
        "email": user.email,
        "mobile": user.mobile,
        "otp_sent_to": otp_sent_to,
        "requires_verification": True,
        "note": "Please check your email and mobile for OTP codes. OTPs expire in 5 minutes."
    }
