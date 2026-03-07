"""
Authentication Service

Handles user registration, authentication, and user retrieval logic.
"""

from typing import Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import hash_password, verify_password


class AuthService:
    """Service class for authentication operations."""

    @staticmethod
    def get_user_by_email(db: Session, email: str) -> Optional[User]:
        """
        Retrieve a user by email address.

        Args:
            db: Database session
            email: User's email address

        Returns:
            User object if found, None otherwise
        """
        return db.query(User).filter(User.email == email).first()

    @staticmethod
    def get_user_by_username(db: Session, username: str) -> Optional[User]:
        """
        Retrieve a user by username.

        Args:
            db: Database session
            username: User's username

        Returns:
            User object if found, None otherwise
        """
        return db.query(User).filter(User.username == username).first()

    @staticmethod
    def get_user_by_id(db: Session, user_id: int) -> Optional[User]:
        """
        Retrieve a user by ID.

        Args:
            db: Database session
            user_id: User's ID

        Returns:
            User object if found, None otherwise
        """
        return db.query(User).filter(User.id == user_id).first()

    @staticmethod
    def authenticate_user(db: Session, email: str, password: str) -> Optional[User]:
        """
        Authenticate a user with email and password.

        Args:
            db: Database session
            email: User's email address
            password: Plain text password

        Returns:
            User object if authentication successful, None otherwise
        """
        user = AuthService.get_user_by_email(db, email)
        if not user:
            return None

        # OAuth users don't have passwords
        if user.oauth_provider:
            return None

        # Check if user has a hashed password
        if not user.hashed_password:
            return None

        if not verify_password(password, user.hashed_password):
            return None
        if not user.is_active:
            return None
        return user

    @staticmethod
    def get_user_by_mobile(db: Session, mobile: str) -> Optional[User]:
        """
        Retrieve a user by mobile number.

        Args:
            db: Database session
            mobile: User's mobile number

        Returns:
            User object if found, None otherwise
        """
        return db.query(User).filter(User.mobile == mobile).first()

    @staticmethod
    def create_user(db: Session, user_data: UserCreate, send_otp: bool = True) -> User:
        """
        Create a new user account.

        Args:
            db: Database session
            user_data: User creation data
            send_otp: Whether to send OTP for verification (default: True)

        Returns:
            Created User object

        Raises:
            HTTPException: If email, username, or mobile already exists
        """
        # Check if email already exists
        existing_user = AuthService.get_user_by_email(db, user_data.email)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )

        # Check if username already exists
        existing_username = AuthService.get_user_by_username(db, user_data.username)
        if existing_username:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already taken"
            )

        # Check if mobile already exists (if provided)
        if user_data.mobile:
            existing_mobile = AuthService.get_user_by_mobile(db, user_data.mobile)
            if existing_mobile:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Mobile number already registered"
                )

        # Hash password only if provided (for manual signup)
        hashed_pwd = None
        if user_data.password:
            hashed_pwd = hash_password(user_data.password)

        # Create new user
        db_user = User(
            email=user_data.email,
            username=user_data.username,
            hashed_password=hashed_pwd,
            full_name=user_data.full_name,
            mobile=user_data.mobile,
            role=user_data.role or "viewer",
            oauth_provider=user_data.oauth_provider,
            oauth_id=user_data.oauth_id,
            email_verified=False if send_otp else True,  # Skip verification for OAuth
            mobile_verified=False,
            is_active=True,
            is_superuser=False
        )

        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return db_user
