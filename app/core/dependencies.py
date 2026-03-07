"""
FastAPI Dependencies

This module provides dependency injection functions for:
- Database session management
- User authentication and authorization
- Role-based access control
"""

from typing import Generator, Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.core.security import decode_access_token
from app.services.auth import AuthService
from app.models.user import User


# OAuth2 scheme for token authentication
# tokenUrl: The endpoint where users get tokens (login endpoint)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


# ==========================================
# Database Dependency
# ==========================================

def get_db() -> Generator:
    """
    Database session dependency.

    Yields a database session and ensures it's closed after use.

    Usage:
        @app.get("/users")
        def get_users(db: Session = Depends(get_db)):
            return db.query(User).all()
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ==========================================
# Authentication Dependencies
# ==========================================

def get_current_user(
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
) -> User:
    """
    Get the current authenticated user from JWT token.

    Args:
        db: Database session
        token: JWT access token from Authorization header

    Returns:
        User object of authenticated user

    Raises:
        HTTPException 401: If token is invalid or user not found

    Usage:
        @app.get("/me")
        def get_me(current_user: User = Depends(get_current_user)):
            return current_user
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    # Decode the JWT token
    payload = decode_access_token(token)
    if payload is None:
        raise credentials_exception

    # Extract user email from token payload
    email: Optional[str] = payload.get("sub")
    if email is None:
        raise credentials_exception

    # Get user from database
    user = AuthService.get_user_by_email(db, email=email)
    if user is None:
        raise credentials_exception

    # Check if user is active
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Inactive user account"
        )

    return user


def get_current_active_user(
    current_user: User = Depends(get_current_user)
) -> User:
    """
    Get current active user (alias for get_current_user).

    This dependency is redundant since get_current_user already checks
    for active status, but kept for clarity and potential future changes.

    Args:
        current_user: User from get_current_user dependency

    Returns:
        Active user object

    Usage:
        @app.get("/profile")
        def get_profile(user: User = Depends(get_current_active_user)):
            return user
    """
    return current_user


# ==========================================
# Role-Based Access Control Dependencies
# ==========================================

def get_current_admin(
    current_user: User = Depends(get_current_user)
) -> User:
    """
    Get current user and verify they have admin role.

    Args:
        current_user: User from get_current_user dependency

    Returns:
        User object if they are an admin

    Raises:
        HTTPException 403: If user is not an admin

    Usage:
        @app.delete("/users/{user_id}")
        def delete_user(user_id: int, admin: User = Depends(get_current_admin)):
            # Only admins can delete users
            ...
    """
    if current_user.role not in ["admin", "auctioneer"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions. Admin or Auctioneer role required."
        )
    return current_user


def get_current_superuser(
    current_user: User = Depends(get_current_user)
) -> User:
    """
    Get current user and verify they are a superuser.

    Args:
        current_user: User from get_current_user dependency

    Returns:
        User object if they are a superuser

    Raises:
        HTTPException 403: If user is not a superuser

    Usage:
        @app.post("/users/make-admin")
        def make_admin(user_id: int, superuser: User = Depends(get_current_superuser)):
            # Only superusers can make other users admins
            ...
    """
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions. Superuser role required."
        )
    return current_user


def get_current_auctioneer(
    current_user: User = Depends(get_current_user)
) -> User:
    """
    Get current user and verify they have auctioneer role.

    Args:
        current_user: User from get_current_user dependency

    Returns:
        User object if they are an auctioneer

    Raises:
        HTTPException 403: If user is not an auctioneer

    Usage:
        @app.post("/auctions/{auction_id}/start")
        def start_auction(auction_id: int, auctioneer: User = Depends(get_current_auctioneer)):
            # Only auctioneers can start auctions
            ...
    """
    if current_user.role != "auctioneer" and not current_user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions. Auctioneer role required."
        )
    return current_user
