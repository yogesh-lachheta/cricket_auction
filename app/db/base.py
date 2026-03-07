"""
Database Base Class

This file contains the SQLAlchemy declarative base class.
All models will inherit from this Base class.
"""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Base class for all database models.

    All SQLAlchemy models should inherit from this class.
    This provides the foundation for the ORM mapping.
    """
    pass
