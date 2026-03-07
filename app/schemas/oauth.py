"""
OAuth Pydantic Schemas

These schemas define the structure for OAuth-related requests and responses.
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional


class OAuthProvider(BaseModel):
    """
    Schema for OAuth provider information.
    """
    provider: str = Field(..., description="OAuth provider (google, microsoft)")
    redirect_uri: str = Field(..., description="Redirect URI after OAuth")

    class Config:
        json_schema_extra = {
            "example": {
                "provider": "google",
                "redirect_uri": "http://localhost:3000/auth/callback"
            }
        }


class OAuthCallback(BaseModel):
    """
    Schema for OAuth callback data.

    In development mode, this accepts manual user data.
    In production, this would process the OAuth code/token.
    """
    provider: str = Field(..., description="OAuth provider (google, microsoft)")

    # Development mode: Manual user data
    email: Optional[EmailStr] = Field(None, description="Email from OAuth provider")
    name: Optional[str] = Field(None, description="Full name from OAuth provider")
    oauth_id: Optional[str] = Field(None, description="OAuth provider user ID")

    # Production mode: OAuth code/token
    code: Optional[str] = Field(None, description="OAuth authorization code")
    access_token: Optional[str] = Field(None, description="OAuth access token")

    class Config:
        json_schema_extra = {
            "example": {
                "provider": "google",
                "email": "user@gmail.com",
                "name": "John Doe",
                "oauth_id": "google-123456789"
            }
        }


class OAuthLoginResponse(BaseModel):
    """
    Schema for OAuth login response.
    """
    authorization_url: Optional[str] = Field(None, description="OAuth authorization URL")
    note: str = Field(..., description="Instructions for OAuth login")

    class Config:
        json_schema_extra = {
            "example": {
                "authorization_url": "https://accounts.google.com/o/oauth2/v2/auth?...",
                "note": "Visit this URL to complete OAuth login"
            }
        }


class OAuthSignupResponse(BaseModel):
    """
    Schema for OAuth signup/callback response.
    """
    success: bool = Field(..., description="Whether signup was successful")
    message: str = Field(..., description="Response message")
    access_token: Optional[str] = Field(None, description="JWT access token")
    token_type: Optional[str] = Field(default="bearer", description="Token type")
    user: Optional[dict] = Field(None, description="User information")

    class Config:
        json_schema_extra = {
            "example": {
                "success": True,
                "message": "Successfully authenticated via Google",
                "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
                "token_type": "bearer",
                "user": {
                    "id": 1,
                    "email": "user@gmail.com",
                    "username": "user_gmail",
                    "oauth_provider": "google"
                }
            }
        }
