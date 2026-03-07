"""
OAuth Service

Handles OAuth authentication with Google and Microsoft.

Development Mode (Default):
- Uses mock OAuth for testing
- No need to register OAuth apps
- Accepts manual user data

Production Mode:
- Set OAUTH_MODE=production in .env
- Requires Google/Microsoft OAuth app credentials
- Handles real OAuth flow
"""

import os
from typing import Optional, Dict
from sqlalchemy.orm import Session

from app.models.user import User
from app.services.auth import AuthService
from app.schemas.user import UserCreate


class OAuthService:
    """Service class for OAuth operations."""

    # OAuth configuration
    OAUTH_MODE = os.getenv("OAUTH_MODE", "development")  # development or production

    # Google OAuth (Production)
    GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID", "")
    GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET", "")
    GOOGLE_REDIRECT_URI = os.getenv("GOOGLE_REDIRECT_URI", "http://localhost:8000/api/v1/auth/google/callback")

    # Microsoft OAuth (Production)
    MICROSOFT_CLIENT_ID = os.getenv("MICROSOFT_CLIENT_ID", "")
    MICROSOFT_CLIENT_SECRET = os.getenv("MICROSOFT_CLIENT_SECRET", "")
    MICROSOFT_REDIRECT_URI = os.getenv("MICROSOFT_REDIRECT_URI", "http://localhost:8000/api/v1/auth/microsoft/callback")

    @staticmethod
    def get_google_auth_url(redirect_uri: Optional[str] = None) -> Dict:
        """
        Get Google OAuth authorization URL.

        Args:
            redirect_uri: Custom redirect URI (optional)

        Returns:
            dict: Authorization URL and instructions
        """
        if OAuthService.OAUTH_MODE == "development":
            return {
                "authorization_url": None,
                "note": "Development Mode: Use POST /api/v1/auth/google/callback with manual user data (email, name, oauth_id)",
                "dev_mode": True,
                "instructions": [
                    "1. Send POST request to /api/v1/auth/google/callback",
                    "2. Include: email, name, oauth_id in request body",
                    "3. System will create user with Google OAuth provider"
                ]
            }

        # Production mode
        base_url = "https://accounts.google.com/o/oauth2/v2/auth"
        redirect = redirect_uri or OAuthService.GOOGLE_REDIRECT_URI

        params = {
            "client_id": OAuthService.GOOGLE_CLIENT_ID,
            "redirect_uri": redirect,
            "response_type": "code",
            "scope": "openid email profile",
            "access_type": "offline",
            "prompt": "consent"
        }

        # Build URL
        param_str = "&".join([f"{k}={v}" for k, v in params.items()])
        auth_url = f"{base_url}?{param_str}"

        return {
            "authorization_url": auth_url,
            "note": "Visit this URL to authenticate with Google",
            "dev_mode": False
        }

    @staticmethod
    def get_microsoft_auth_url(redirect_uri: Optional[str] = None) -> Dict:
        """
        Get Microsoft OAuth authorization URL.

        Args:
            redirect_uri: Custom redirect URI (optional)

        Returns:
            dict: Authorization URL and instructions
        """
        if OAuthService.OAUTH_MODE == "development":
            return {
                "authorization_url": None,
                "note": "Development Mode: Use POST /api/v1/auth/microsoft/callback with manual user data (email, name, oauth_id)",
                "dev_mode": True,
                "instructions": [
                    "1. Send POST request to /api/v1/auth/microsoft/callback",
                    "2. Include: email, name, oauth_id in request body",
                    "3. System will create user with Microsoft OAuth provider"
                ]
            }

        # Production mode
        base_url = "https://login.microsoftonline.com/common/oauth2/v2.0/authorize"
        redirect = redirect_uri or OAuthService.MICROSOFT_REDIRECT_URI

        params = {
            "client_id": OAuthService.MICROSOFT_CLIENT_ID,
            "redirect_uri": redirect,
            "response_type": "code",
            "scope": "openid email profile",
            "response_mode": "query"
        }

        # Build URL
        param_str = "&".join([f"{k}={v}" for k, v in params.items()])
        auth_url = f"{base_url}?{param_str}"

        return {
            "authorization_url": auth_url,
            "note": "Visit this URL to authenticate with Microsoft",
            "dev_mode": False
        }

    @staticmethod
    def create_or_get_oauth_user(
        db: Session,
        provider: str,
        email: str,
        name: str,
        oauth_id: str
    ) -> User:
        """
        Create or get user from OAuth data.

        Args:
            db: Database session
            provider: OAuth provider (google, microsoft)
            email: User email from OAuth
            name: User full name from OAuth
            oauth_id: OAuth provider user ID

        Returns:
            User: Created or existing user
        """
        # Check if user already exists with this OAuth ID
        existing_user = db.query(User).filter(
            User.oauth_provider == provider,
            User.oauth_id == oauth_id
        ).first()

        if existing_user:
            print(f"✅ Existing OAuth user found: {existing_user.email}")
            return existing_user

        # Check if email already exists
        email_user = AuthService.get_user_by_email(db, email)
        if email_user:
            # Update existing user with OAuth info
            if not email_user.oauth_provider:
                email_user.oauth_provider = provider
                email_user.oauth_id = oauth_id
                email_user.email_verified = True  # OAuth emails are pre-verified
                db.commit()
                db.refresh(email_user)
                print(f"✅ Updated existing user with OAuth: {email_user.email}")
                return email_user
            else:
                # User exists with different OAuth provider
                raise ValueError(f"Email {email} already registered with {email_user.oauth_provider}")

        # Create username from email
        username = email.split("@")[0]
        base_username = username

        # Ensure username is unique
        counter = 1
        while AuthService.get_user_by_username(db, username):
            username = f"{base_username}{counter}"
            counter += 1

        # Create new OAuth user
        user_data = UserCreate(
            email=email,
            username=username,
            full_name=name,
            password=None,  # No password for OAuth users
            oauth_provider=provider,
            oauth_id=oauth_id,
            role="viewer"
        )

        # Create user without OTP (OAuth users don't need OTP)
        user = AuthService.create_user(db, user_data, send_otp=False)

        # Mark as verified
        user.email_verified = True
        db.commit()
        db.refresh(user)

        print(f"✅ New OAuth user created: {user.email} via {provider}")
        return user

    @staticmethod
    def handle_google_callback(
        db: Session,
        email: Optional[str] = None,
        name: Optional[str] = None,
        oauth_id: Optional[str] = None,
        code: Optional[str] = None
    ) -> User:
        """
        Handle Google OAuth callback.

        Development mode: Uses provided email, name, oauth_id
        Production mode: Exchanges code for user info

        Args:
            db: Database session
            email: User email (dev mode)
            name: User name (dev mode)
            oauth_id: OAuth ID (dev mode)
            code: Authorization code (production mode)

        Returns:
            User: Created or existing user
        """
        if OAuthService.OAUTH_MODE == "development":
            # Development mode: Use provided data
            if not all([email, name, oauth_id]):
                raise ValueError("In development mode, email, name, and oauth_id are required")

            return OAuthService.create_or_get_oauth_user(
                db=db,
                provider="google",
                email=email,
                name=name,
                oauth_id=oauth_id
            )

        # Production mode: Exchange code for user info
        # TODO: Implement real Google OAuth token exchange
        # This would use the 'code' to get access token, then fetch user info
        raise NotImplementedError("Production Google OAuth not yet implemented. Set OAUTH_MODE=development")

    @staticmethod
    def handle_microsoft_callback(
        db: Session,
        email: Optional[str] = None,
        name: Optional[str] = None,
        oauth_id: Optional[str] = None,
        code: Optional[str] = None
    ) -> User:
        """
        Handle Microsoft OAuth callback.

        Development mode: Uses provided email, name, oauth_id
        Production mode: Exchanges code for user info

        Args:
            db: Database session
            email: User email (dev mode)
            name: User name (dev mode)
            oauth_id: OAuth ID (dev mode)
            code: Authorization code (production mode)

        Returns:
            User: Created or existing user
        """
        if OAuthService.OAUTH_MODE == "development":
            # Development mode: Use provided data
            if not all([email, name, oauth_id]):
                raise ValueError("In development mode, email, name, and oauth_id are required")

            return OAuthService.create_or_get_oauth_user(
                db=db,
                provider="microsoft",
                email=email,
                name=name,
                oauth_id=oauth_id
            )

        # Production mode: Exchange code for user info
        # TODO: Implement real Microsoft OAuth token exchange
        raise NotImplementedError("Production Microsoft OAuth not yet implemented. Set OAUTH_MODE=development")
