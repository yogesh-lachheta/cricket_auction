"""
User Pydantic Schemas

These schemas define the structure for user-related requests and responses.
They provide automatic validation and serialization.
"""

from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field, validator, model_validator


class UserBase(BaseModel):
    """
    Base User schema with common fields.

    This is the parent class that other schemas inherit from.
    """
    email: EmailStr = Field(..., description="User's email address")
    username: str = Field(..., min_length=3, max_length=100, description="Unique username")
    full_name: Optional[str] = Field(None, max_length=200, description="User's full name")
    mobile: Optional[str] = Field(None, max_length=20, description="Mobile number with country code (e.g., +919876543210)")
    role: str = Field(default="viewer", description="User role: admin, team_owner, or viewer")

    @validator("role")
    def validate_role(cls, v):
        """Validate that role is one of the allowed values"""
        allowed_roles = ["admin", "team_owner", "viewer", "auctioneer"]
        if v not in allowed_roles:
            raise ValueError(f"Role must be one of: {', '.join(allowed_roles)}")
        return v

    @validator("mobile")
    def validate_mobile(cls, v):
        """Validate mobile number format (must start with + and have 10-15 digits)"""
        if v is not None:
            # Remove spaces and dashes for validation
            clean_mobile = v.replace(" ", "").replace("-", "")
            if not clean_mobile.startswith("+"):
                raise ValueError("Mobile number must start with country code (e.g., +91)")
            if not clean_mobile[1:].isdigit():
                raise ValueError("Mobile number must contain only digits after country code")
            if len(clean_mobile[1:]) < 10 or len(clean_mobile[1:]) > 15:
                raise ValueError("Mobile number must have 10-15 digits")
        return v


class UserCreate(UserBase):
    """
    Schema for creating a new user.

    Used when registering a new account.
    Includes password field for creation (optional for OAuth users).
    """
    password: Optional[str] = Field(
        None,
        min_length=8,
        max_length=100,
        description="User password (min 8 characters, required for manual signup)"
    )
    oauth_provider: Optional[str] = Field(None, description="OAuth provider (google, microsoft)")
    oauth_id: Optional[str] = Field(None, description="OAuth provider user ID")

    @model_validator(mode='after')
    def validate_password_or_oauth(self):
        """
        Validate that either password or OAuth is provided.

        Password must contain:
        - At least 8 characters
        - At least one lowercase letter
        - At least one uppercase letter
        - At least one digit

        Password is required for manual signup (when oauth_provider is None).
        OAuth users don't need passwords.
        """
        password = self.password
        oauth_provider = self.oauth_provider

        # If not OAuth signup, password is required
        if oauth_provider is None and password is None:
            raise ValueError("Password is required for manual signup")

        # If password is provided, validate strength
        if password is not None:
            if len(password) < 8:
                raise ValueError("Password must be at least 8 characters long")

            if not any(char.islower() for char in password):
                raise ValueError("Password must contain at least one lowercase letter")

            if not any(char.isupper() for char in password):
                raise ValueError("Password must contain at least one uppercase letter")

            if not any(char.isdigit() for char in password):
                raise ValueError("Password must contain at least one digit")

        return self


class UserUpdate(BaseModel):
    """
    Schema for updating user information.

    All fields are optional so users can update specific fields only.
    """
    email: Optional[EmailStr] = None
    username: Optional[str] = Field(None, min_length=3, max_length=100)
    full_name: Optional[str] = Field(None, max_length=200)
    role: Optional[str] = None
    is_active: Optional[bool] = None

    @validator("role")
    def validate_role(cls, v):
        """Validate that role is one of the allowed values"""
        if v is not None:
            allowed_roles = ["admin", "team_owner", "viewer"]
            if v not in allowed_roles:
                raise ValueError(f"Role must be one of: {', '.join(allowed_roles)}")
        return v


class UserInDB(UserBase):
    """
    Schema for user data as stored in database.

    Includes all fields including timestamps and flags.
    Used internally, not returned to clients directly.
    """
    id: int
    hashed_password: str
    is_active: bool
    is_superuser: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        """Pydantic configuration"""
        from_attributes = True  # Allows creating from ORM models


class UserResponse(UserBase):
    """
    Schema for user data in API responses.

    Excludes sensitive information like hashed_password.
    This is what gets returned to API clients.
    """
    id: int
    oauth_provider: Optional[str] = None
    oauth_id: Optional[str] = None
    email_verified: bool = False
    mobile_verified: bool = False
    is_active: bool
    is_superuser: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        """Pydantic configuration"""
        from_attributes = True  # Allows creating from ORM models
        json_schema_extra = {
            "example": {
                "id": 1,
                "email": "user@example.com",
                "username": "johndoe",
                "full_name": "John Doe",
                "mobile": "+919876543210",
                "role": "team_owner",
                "oauth_provider": None,
                "oauth_id": None,
                "email_verified": True,
                "mobile_verified": True,
                "is_active": True,
                "is_superuser": False,
                "created_at": "2024-01-01T00:00:00Z",
                "updated_at": "2024-01-01T00:00:00Z"
            }
        }


class UserLogin(BaseModel):
    """
    Schema for user login request.

    Used in login endpoint to authenticate users.
    """
    email: EmailStr = Field(..., description="User's email address")
    password: str = Field(..., description="User's password")

    class Config:
        json_schema_extra = {
            "example": {
                "email": "user@example.com",
                "password": "SecurePass123"
            }
        }
