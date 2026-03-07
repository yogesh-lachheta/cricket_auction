"""
Security utilities for password hashing and JWT token management.

This module provides functions for:
- Password hashing and verification using bcrypt
- JWT token creation and validation
"""

from datetime import datetime, timedelta
from typing import Optional, Union, Any
from jose import jwt, JWTError
from passlib.context import CryptContext
from app.core.config import settings


# Password Hashing Configuration
# CryptContext: Manages password hashing schemes (using bcrypt)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# ==========================================
# Password Hashing Functions
# ==========================================

def hash_password(password: str) -> str:
    """
    Hash a plain text password using bcrypt.

    Args:
        password (str): Plain text password to hash

    Returns:
        str: Hashed password string

    Example:
        hashed = hash_password("mypassword123")
        # Returns: "$2b$12$abcd..."
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a plain text password against a hashed password.

    Args:
        plain_password (str): Plain text password to verify
        hashed_password (str): Hashed password from database

    Returns:
        bool: True if password matches, False otherwise

    Example:
        is_valid = verify_password("mypassword123", "$2b$12$abcd...")
        # Returns: True if correct, False if wrong
    """
    return pwd_context.verify(plain_password, hashed_password)


# ==========================================
# JWT Token Functions
# ==========================================

def create_access_token(
    data: dict,
    expires_delta: Optional[timedelta] = None
) -> str:
    """
    Create a JWT access token with expiration.

    Args:
        data (dict): Payload data to encode in token (usually user info)
        expires_delta (timedelta, optional): Custom expiration time
            If not provided, uses default from settings (30 minutes)

    Returns:
        str: Encoded JWT token string

    Example:
        token = create_access_token({"sub": "user@example.com"})
        # Returns: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
    """
    # Make a copy of the data to avoid modifying the original
    to_encode = data.copy()

    # Calculate expiration time
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        # Use default expiration from settings (30 minutes)
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )

    # Add expiration time to payload
    to_encode.update({"exp": expire})

    # Encode the JWT token
    # Uses SECRET_KEY and ALGORITHM from settings
    encoded_jwt = jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

    return encoded_jwt


def decode_access_token(token: str) -> Optional[dict]:
    """
    Decode and verify a JWT access token.

    Args:
        token (str): JWT token string to decode

    Returns:
        dict: Decoded token payload if valid, None if invalid

    Example:
        payload = decode_access_token("eyJhbGciOi...")
        # Returns: {"sub": "user@example.com", "exp": 1234567890}
        # Returns: None if token is invalid or expired
    """
    try:
        # Decode the JWT token
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        return payload
    except JWTError:
        # Token is invalid, expired, or tampered with
        return None
