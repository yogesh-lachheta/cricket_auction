"""
OTP Service

Handles OTP generation, storage, verification, and sending.
"""

import random
import string
from datetime import datetime, timedelta, timezone
from typing import Optional
from sqlalchemy.orm import Session

from app.models.otp import OTP, OTPType
from app.models.user import User


class OTPService:
    """Service class for OTP operations."""

    # OTP expires in 5 minutes
    OTP_EXPIRY_MINUTES = 5

    @staticmethod
    def generate_otp_code() -> str:
        """
        Generate a random 6-digit OTP code.

        Returns:
            str: 6-digit OTP code
        """
        return ''.join(random.choices(string.digits, k=6))

    @staticmethod
    def create_otp(
        db: Session,
        user_id: int,
        otp_type: OTPType,
        recipient: str
    ) -> OTP:
        """
        Create a new OTP record.

        Args:
            db: Database session
            user_id: User ID
            otp_type: Type of OTP (EMAIL or MOBILE)
            recipient: Email address or mobile number

        Returns:
            OTP: Created OTP object
        """
        # Generate OTP code
        code = OTPService.generate_otp_code()

        # Calculate expiration time
        expires_at = datetime.now(timezone.utc) + timedelta(
            minutes=OTPService.OTP_EXPIRY_MINUTES
        )

        # Invalidate any previous unused OTPs for this user and type
        db.query(OTP).filter(
            OTP.user_id == user_id,
            OTP.otp_type == otp_type,
            OTP.is_used == False,
            OTP.is_verified == False
        ).update({
            "is_used": True
        })
        db.commit()

        # Create new OTP
        otp = OTP(
            user_id=user_id,
            otp_type=otp_type,
            code=code,
            recipient=recipient,
            expires_at=expires_at,
            is_used=False,
            is_verified=False
        )

        db.add(otp)
        db.commit()
        db.refresh(otp)

        return otp

    @staticmethod
    def verify_otp(
        db: Session,
        user_id: int,
        otp_type: OTPType,
        code: str
    ) -> bool:
        """
        Verify an OTP code.

        Args:
            db: Database session
            user_id: User ID
            otp_type: Type of OTP (EMAIL or MOBILE)
            code: OTP code to verify

        Returns:
            bool: True if OTP is valid, False otherwise
        """
        # Find the OTP
        otp = db.query(OTP).filter(
            OTP.user_id == user_id,
            OTP.otp_type == otp_type,
            OTP.code == code,
            OTP.is_used == False
        ).first()

        if not otp:
            return False

        # Check if OTP has expired
        if datetime.now(timezone.utc) > otp.expires_at:
            otp.is_used = True
            db.commit()
            return False

        # Mark OTP as used and verified
        otp.is_used = True
        otp.is_verified = True
        db.commit()

        # Update user verification status
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            if otp_type == OTPType.EMAIL:
                user.email_verified = True
            elif otp_type == OTPType.MOBILE:
                user.mobile_verified = True
            db.commit()

        return True

    @staticmethod
    def get_latest_otp(
        db: Session,
        user_id: int,
        otp_type: OTPType
    ) -> Optional[OTP]:
        """
        Get the latest OTP for a user and type.

        Args:
            db: Database session
            user_id: User ID
            otp_type: Type of OTP (EMAIL or MOBILE)

        Returns:
            OTP: Latest OTP object or None
        """
        return db.query(OTP).filter(
            OTP.user_id == user_id,
            OTP.otp_type == otp_type
        ).order_by(OTP.created_at.desc()).first()

    @staticmethod
    def is_otp_valid(otp: OTP) -> bool:
        """
        Check if an OTP is still valid (not expired, not used).

        Args:
            otp: OTP object

        Returns:
            bool: True if OTP is valid, False otherwise
        """
        if otp.is_used:
            return False

        if datetime.now(timezone.utc) > otp.expires_at:
            return False

        return True
