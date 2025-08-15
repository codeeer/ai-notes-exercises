"""
User Pydantic schemas for request/response validation.
Comprehensive schemas with validation rules.
"""
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field, validator


# Base schemas
class UserBase(BaseModel):
    """Base user schema with common fields."""
    email: str  # EmailStr yerine str kullanıyoruz (dependency sorunları için)
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    full_name: Optional[str] = Field(None, max_length=100)
    bio: Optional[str] = Field(None, max_length=500)
    phone: Optional[str] = None
    
    @validator('username')
    def validate_username(cls, v):
        if v is not None:
            if not v.replace('_', '').isalnum():  # Allow underscores
                raise ValueError('Username must be alphanumeric')
        return v


class UserCreate(UserBase):
    """Schema for user creation."""
    password: str = Field(..., min_length=8, max_length=100)
    confirm_password: str
    
    @validator('confirm_password')
    def passwords_match(cls, v, values):
        if 'password' in values and v != values['password']:
            raise ValueError('Passwords do not match')
        return v
    
    @validator('password')
    def validate_password(cls, v):
        if not any(c.isupper() for c in v):
            raise ValueError('Password must contain at least one uppercase letter')
        if not any(c.islower() for c in v):
            raise ValueError('Password must contain at least one lowercase letter')
        if not any(c.isdigit() for c in v):
            raise ValueError('Password must contain at least one digit')
        return v


class UserUpdate(BaseModel):
    """Schema for user updates (all fields optional)."""
    email: Optional[str] = None
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    full_name: Optional[str] = Field(None, max_length=100)
    bio: Optional[str] = Field(None, max_length=500)
    phone: Optional[str] = None
    is_active: Optional[bool] = None
    
    @validator('username')
    def validate_username(cls, v):
        if v is not None and not v.replace('_', '').isalnum():
            raise ValueError('Username must be alphanumeric')
        return v


class UserResponse(UserBase):
    """Schema for user responses (public data)."""
    id: int
    is_active: bool
    is_verified: bool
    created_at: datetime
    updated_at: datetime
    last_login: Optional[datetime] = None
    login_count: int
    
    class Config:
        from_attributes = True  # Pydantic v2 için orm_mode yerine


class UserDetail(UserResponse):
    """Detailed user schema (for authenticated users)."""
    is_superuser: bool
    avatar_url: Optional[str] = None


class UserInDB(UserDetail):
    """Internal schema with sensitive data."""
    hashed_password: str


# Password change schema
class PasswordChange(BaseModel):
    """Schema for password change."""
    current_password: str
    new_password: str = Field(..., min_length=8, max_length=100)
    confirm_new_password: str
    
    @validator('confirm_new_password')
    def passwords_match(cls, v, values):
        if 'new_password' in values and v != values['new_password']:
            raise ValueError('New passwords do not match')
        return v


# Login schemas
class UserLogin(BaseModel):
    """Schema for user login."""
    email: str
    password: str


class Token(BaseModel):
    """Token response schema."""
    access_token: str
    token_type: str = "bearer"
    expires_in: int


class TokenData(BaseModel):
    """Token payload data."""
    user_id: Optional[int] = None
    email: Optional[str] = None


# Pagination schema
class UserListResponse(BaseModel):
    """Paginated user list response."""
    users: list[UserResponse]
    total: int
    page: int
    page_size: int
    total_pages: int