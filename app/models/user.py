"""
User Database Model

This module defines the User table structure in the database.
Users can be admins, team owners, or viewers.
"""

from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.db.base import Base


class User(Base):
    """
    User model for authentication and authorization.

    This table stores all user information including credentials,
    roles, and account status.

    Attributes:
        id: Primary key
        email: Unique email address (used for login)
        username: Unique username
        hashed_password: Bcrypt hashed password (never store plain passwords!)
        full_name: User's full name
        role: User role (admin, team_owner, viewer)
        is_active: Account active status
        is_superuser: Admin privileges flag
        created_at: Account creation timestamp
        updated_at: Last update timestamp
    """

    __tablename__ = "users"

    # Primary Key
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    # Authentication Fields
    email = Column(String(255), unique=True, index=True, nullable=False)
    username = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)

    # User Information
    full_name = Column(String(200), nullable=True)

    # Role & Permissions
    role = Column(
        String(50),
        nullable=False,
        default="viewer",
        comment="User role: admin, team_owner, or viewer"
    )

    # Account Status
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)

    # Timestamps
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

    def __repr__(self):
        """String representation of User object"""
        return f"<User(id={self.id}, email='{self.email}', role='{self.role}')>"
