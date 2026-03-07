"""
Token Pydantic Schemas

These schemas define the structure for authentication tokens and responses.
"""

from typing import Optional
from pydantic import BaseModel, Field


class Token(BaseModel):
    """
    Schema for JWT token response.

    This is what the API returns when a user logs in successfully.
    """
    access_token: str = Field(..., description="JWT access token")
    token_type: str = Field(default="bearer", description="Token type (always 'bearer')")

    class Config:
        json_schema_extra = {
            "example": {
                "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
                "token_type": "bearer"
            }
        }


class TokenPayload(BaseModel):
    """
    Schema for JWT token payload (what's inside the token).

    This is the data that gets encoded into the JWT token.
    """
    sub: Optional[str] = Field(None, description="Subject (usually user email or ID)")
    exp: Optional[int] = Field(None, description="Expiration timestamp")

    class Config:
        json_schema_extra = {
            "example": {
                "sub": "user@example.com",
                "exp": 1234567890
            }
        }
