"""
OAuth Authentication Endpoints

Supports Google and Microsoft OAuth login.

Development Mode (Default):
- No OAuth app registration needed
- Use mock OAuth data for testing
- POST to /google/callback or /microsoft/callback with user data

Production Mode:
- Set OAUTH_MODE=production in .env
- Configure OAuth app credentials
- Follow standard OAuth flow
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.core.security import create_access_token
from app.schemas.oauth import OAuthCallback, OAuthLoginResponse, OAuthSignupResponse
from app.schemas.user import UserResponse
from app.services.oauth_service import OAuthService


router = APIRouter()


# ==========================================
# Google OAuth Endpoints
# ==========================================

@router.get(
    "/google",
    response_model=OAuthLoginResponse,
    summary="Get Google OAuth login URL",
    description="Returns Google OAuth authorization URL (or dev mode instructions)"
)
def google_login():
    """
    Get Google OAuth login URL.

    Development Mode:
    - Returns instructions for manual OAuth testing
    - No OAuth app registration needed

    Production Mode:
    - Returns Google OAuth authorization URL
    - User clicks URL to authenticate

    Returns:
        OAuthLoginResponse: Authorization URL or instructions
    """
    auth_data = OAuthService.get_google_auth_url()
    return OAuthLoginResponse(**auth_data)


@router.post(
    "/google/callback",
    response_model=OAuthSignupResponse,
    summary="Google OAuth callback",
    description="Handle Google OAuth callback and create/login user"
)
def google_callback(
    oauth_data: OAuthCallback,
    db: Session = Depends(get_db)
):
    """
    Handle Google OAuth callback.

    Development Mode:
    - Send: {"provider": "google", "email": "user@gmail.com", "name": "John Doe", "oauth_id": "google-123"}
    - Creates user with Google OAuth provider
    - Returns JWT token for immediate login

    Production Mode:
    - Receives OAuth authorization code
    - Exchanges code for user info
    - Creates/logins user

    Args:
        oauth_data: OAuth callback data
        db: Database session

    Returns:
        OAuthSignupResponse: Success status and JWT token

    Raises:
        HTTPException 400: If OAuth data is invalid
        HTTPException 500: If OAuth processing fails
    """
    try:
        # Handle Google OAuth callback
        user = OAuthService.handle_google_callback(
            db=db,
            email=oauth_data.email,
            name=oauth_data.name,
            oauth_id=oauth_data.oauth_id,
            code=oauth_data.code
        )

        # Create JWT token
        access_token = create_access_token(data={"sub": user.email})

        return OAuthSignupResponse(
            success=True,
            message=f"Successfully authenticated via Google",
            access_token=access_token,
            token_type="bearer",
            user=UserResponse.model_validate(user).model_dump()
        )

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"OAuth authentication failed: {str(e)}"
        )


# ==========================================
# Microsoft OAuth Endpoints
# ==========================================

@router.get(
    "/microsoft",
    response_model=OAuthLoginResponse,
    summary="Get Microsoft OAuth login URL",
    description="Returns Microsoft OAuth authorization URL (or dev mode instructions)"
)
def microsoft_login():
    """
    Get Microsoft OAuth login URL.

    Development Mode:
    - Returns instructions for manual OAuth testing
    - No OAuth app registration needed

    Production Mode:
    - Returns Microsoft OAuth authorization URL
    - User clicks URL to authenticate

    Returns:
        OAuthLoginResponse: Authorization URL or instructions
    """
    auth_data = OAuthService.get_microsoft_auth_url()
    return OAuthLoginResponse(**auth_data)


@router.post(
    "/microsoft/callback",
    response_model=OAuthSignupResponse,
    summary="Microsoft OAuth callback",
    description="Handle Microsoft OAuth callback and create/login user"
)
def microsoft_callback(
    oauth_data: OAuthCallback,
    db: Session = Depends(get_db)
):
    """
    Handle Microsoft OAuth callback.

    Development Mode:
    - Send: {"provider": "microsoft", "email": "user@outlook.com", "name": "Jane Doe", "oauth_id": "ms-456"}
    - Creates user with Microsoft OAuth provider
    - Returns JWT token for immediate login

    Production Mode:
    - Receives OAuth authorization code
    - Exchanges code for user info
    - Creates/logins user

    Args:
        oauth_data: OAuth callback data
        db: Database session

    Returns:
        OAuthSignupResponse: Success status and JWT token

    Raises:
        HTTPException 400: If OAuth data is invalid
        HTTPException 500: If OAuth processing fails
    """
    try:
        # Handle Microsoft OAuth callback
        user = OAuthService.handle_microsoft_callback(
            db=db,
            email=oauth_data.email,
            name=oauth_data.name,
            oauth_id=oauth_data.oauth_id,
            code=oauth_data.code
        )

        # Create JWT token
        access_token = create_access_token(data={"sub": user.email})

        return OAuthSignupResponse(
            success=True,
            message=f"Successfully authenticated via Microsoft",
            access_token=access_token,
            token_type="bearer",
            user=UserResponse.model_validate(user).model_dump()
        )

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"OAuth authentication failed: {str(e)}"
        )
