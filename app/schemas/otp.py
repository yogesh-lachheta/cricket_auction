"""
OTP Pydantic Schemas

These schemas define the structure for OTP-related requests and responses.
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional


class OTPRequest(BaseModel):
    """
    Schema for requesting OTP (resend).

    Used when user wants to resend OTP.
    """
    email: Optional[EmailStr] = Field(None, description="Email address for OTP")
    mobile: Optional[str] = Field(None, description="Mobile number for OTP")

    class Config:
        json_schema_extra = {
            "example": {
                "email": "user@example.com",
                "mobile": "+919876543210"
            }
        }


class OTPVerify(BaseModel):
    """
    Schema for verifying OTP.

    Used when user submits OTP code for verification.
    """
    email: Optional[EmailStr] = Field(None, description="Email address (for email OTP)")
    mobile: Optional[str] = Field(None, description="Mobile number (for mobile OTP)")
    otp_code: str = Field(..., min_length=6, max_length=6, description="6-digit OTP code")

    class Config:
        json_schema_extra = {
            "example": {
                "email": "user@example.com",
                "otp_code": "123456"
            }
        }


class OTPResponse(BaseModel):
    """
    Schema for OTP response.

    Returned after OTP is sent or verified.
    """
    success: bool = Field(..., description="Whether operation was successful")
    message: str = Field(..., description="Response message")
    otp_sent_to: Optional[str] = Field(None, description="Where OTP was sent (email/mobile)")
    expires_in_minutes: Optional[int] = Field(None, description="OTP expiration time in minutes")

    class Config:
        json_schema_extra = {
            "example": {
                "success": True,
                "message": "OTP sent successfully",
                "otp_sent_to": "user@example.com",
                "expires_in_minutes": 5
            }
        }
