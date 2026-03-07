"""
User Login Endpoint
"""

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.core.dependencies import get_db, get_current_user
from app.core.security import create_access_token
from app.schemas.token import Token
from app.schemas.user import UserResponse
from app.services.auth import AuthService


router = APIRouter()


@router.post(
    "/login",
    response_model=Token,
    summary="User login",
    description="Authenticate user and return JWT access token"
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    """
    User login endpoint.

    Authenticates user with email/username and password, returns JWT token.

    Args:
        form_data: OAuth2 form with username (email) and password
        db: Database session

    Returns:
        Token: JWT access token and token type

    Raises:
        HTTPException 401: If credentials are invalid
    """
    # Authenticate user
    user = AuthService.authenticate_user(
        db,
        email=form_data.username,  # OAuth2 uses 'username' but we use email
        password=form_data.password
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Create access token
    access_token = create_access_token(data={"sub": user.email})

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.get(
    "/me",
    response_model=UserResponse,
    summary="Get current user",
    description="Get details of currently authenticated user"
)
def get_me(
    current_user: UserResponse = Depends(get_current_user)
):
    """
    Get current authenticated user details.

    This is a protected endpoint that requires a valid JWT token.

    Args:
        current_user: Current authenticated user from JWT token

    Returns:
        UserResponse: Current user details
    """
    return current_user
