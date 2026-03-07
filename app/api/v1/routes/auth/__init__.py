"""
Authentication Routes Module

Combines all authentication-related endpoints.
"""

from fastapi import APIRouter
from app.api.v1.routes.auth import register, login, otp, oauth


router = APIRouter()

# Include authentication endpoints
router.include_router(register.router, tags=["Authentication"])
router.include_router(login.router, tags=["Authentication"])
router.include_router(otp.router, tags=["OTP Verification"])
router.include_router(oauth.router, tags=["OAuth (Google & Microsoft)"])
