from typing import List
from pydantic_settings import BaseSettings
from pydantic import AnyHttpUrl, validator
import secrets


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    Uses pydantic-settings to automatically load from .env file.
    """

    # API Configuration
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Cricket Auction Platform"
    DEBUG: bool = True

    # Security Configuration
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Database Configuration
    DATABASE_URL: str
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_NAME: str = "cricket_auction"
    DB_USER: str = "admin"
    DB_PASSWORD: str = "admin"

    # CORS Configuration
    BACKEND_CORS_ORIGINS: str = "http://localhost:3000,http://localhost:8000,http://localhost:8001"

    @property
    def cors_origins(self) -> List[str]:
        """Parse CORS origins from string"""
        if isinstance(self.BACKEND_CORS_ORIGINS, str):
            return [i.strip() for i in self.BACKEND_CORS_ORIGINS.split(",")]
        return self.BACKEND_CORS_ORIGINS

    # Application Settings
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    class Config:
        """Pydantic configuration"""
        env_file = ".env"
        case_sensitive = True


# Create global settings instance
settings = Settings()
