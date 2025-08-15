"""
Application configuration using Pydantic settings.
Environment-based configuration with validation.
"""
from typing import List
from pydantic import BaseModel
import os

# Load environment variables
from dotenv import load_dotenv
load_dotenv(override=True)


class Settings(BaseModel):
    """Application settings with environment variable support."""
    
    # Application
    APP_NAME: str = "Modern User API"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True
    
    # Database - FIXED DATABASE_URL
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql+asyncpg://omer:@localhost:5432/modern_user_api")
    
    # Security
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    ALGORITHM: str = "HS256"
    
    # CORS
    BACKEND_CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:8000",
        "http://localhost:8080",
    ]
    
    # API
    API_V1_STR: str = "/api/v1"
    
    # Pagination
    DEFAULT_PAGE_SIZE: int = 20
    MAX_PAGE_SIZE: int = 100


# Global settings instance
settings = Settings()

# Debug print
print(f"🔧 Using DATABASE_URL: {settings.DATABASE_URL}")