"""
OTP (One-Time Password) Database Model

This module defines the OTP table for email and mobile verification.
"""

from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum
from app.db.base import Base


class OTPType(str, enum.Enum):
    """Enum for OTP types"""
    EMAIL = "email"
    MOBILE = "mobile"


class OTP(Base):
    """
    OTP model for email and mobile verification.

    Attributes:
        id: Primary key
        user_id: Foreign key to user
        otp_type: Type of OTP (email or mobile)
        code: 6-digit OTP code
        recipient: Email address or mobile number
        expires_at: Expiration timestamp (5 minutes from creation)
        is_used: Whether the OTP has been used
        is_verified: Whether the OTP was successfully verified
        created_at: OTP generation timestamp
    """

    __tablename__ = "otps"

    # Primary Key
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    # User Reference
    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    # OTP Details
    otp_type = Column(
        Enum(OTPType),
        nullable=False,
        comment="Type of OTP: email or mobile"
    )
    code = Column(String(6), nullable=False, comment="6-digit OTP code")
    recipient = Column(
        String(255),
        nullable=False,
        comment="Email address or mobile number"
    )

    # Status
    expires_at = Column(
        DateTime(timezone=True),
        nullable=False,
        comment="OTP expiration time (5 minutes)"
    )
    is_used = Column(Boolean, default=False, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)

    # Timestamp
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    # Relationships
    user = relationship("User", backref="otps")

    def __repr__(self):
        """String representation of OTP object"""
        return f"<OTP(id={self.id}, type='{self.otp_type}', recipient='{self.recipient}', used={self.is_used})>"
