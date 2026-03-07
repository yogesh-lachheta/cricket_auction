"""
Database Session Management

This module handles database connection and session management.
It creates the SQLAlchemy engine and session factory.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Create database engine
# echo=True will log all SQL statements (useful for debugging)
# pool_pre_ping=True ensures connections are alive before using them
engine = create_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,  # Log SQL in debug mode
    pool_pre_ping=True,   # Verify connections before use
    pool_size=5,          # Connection pool size
    max_overflow=10       # Max overflow connections
)

# Create SessionLocal class
# Each instance will be a database session
SessionLocal = sessionmaker(
    autocommit=False,  # Don't auto-commit transactions
    autoflush=False,   # Don't auto-flush before queries
    bind=engine        # Bind to our engine
)


def get_db():
    """
    Dependency function for FastAPI routes.

    Provides a database session and ensures it's closed after use.

    Usage in FastAPI routes:
        @app.get("/users/")
        def get_users(db: Session = Depends(get_db)):
            return db.query(User).all()

    Yields:
        Session: SQLAlchemy database session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
