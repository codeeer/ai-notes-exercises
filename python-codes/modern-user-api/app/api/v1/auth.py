"""
Authentication endpoints for login, register, and token management.
Modern JWT authentication with comprehensive error handling.
"""
from datetime import timedelta
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.api.dependencies import get_current_user, get_user_service
from app.core.config import settings
from app.core.security import create_access_token
from app.models.user import User
from app.schemas.user import (
    PasswordChange,
    Token,
    UserCreate,
    UserDetail,
    UserLogin,
    UserResponse
)
from app.schemas.user import (
    PasswordChange,
    Token,
    UserCreate,
    UserDetail,
    UserLogin,
    UserResponse,
    UserUpdate  # Bu eksikti!
)
from app.services.user import UserService

router = APIRouter()


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register(
    user_data: UserCreate,
    user_service: UserService = Depends(get_user_service)
) -> Any:
    """
    Register a new user.
    
    - **email**: Valid email address (must be unique)
    - **password**: Strong password (min 8 chars, upper, lower, digit)
    - **username**: Optional username (must be unique if provided)
    - **full_name**: Optional full name
    """
    try:
        user = await user_service.create_user(user_data)
        return user
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Registration failed"
        )


@router.post("/login", response_model=Token)
async def login(
    login_data: UserLogin,
    user_service: UserService = Depends(get_user_service)
) -> Any:
    """
    Login user and return access token.
    
    - **email**: User email
    - **password**: User password
    
    Returns JWT access token for API authentication.
    """
    user = await user_service.authenticate_user(
        login_data.email, 
        login_data.password
    )
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Create access token
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(user.id), "email": user.email},
        expires_delta=access_token_expires
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "expires_in": settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60  # in seconds
    }


@router.post("/login/form", response_model=Token)
async def login_form(
    form_data: OAuth2PasswordRequestForm = Depends(),
    user_service: UserService = Depends(get_user_service)
) -> Any:
    """
    OAuth2 compatible login endpoint for Swagger UI.
    
    Uses username field for email address.
    """
    user = await user_service.authenticate_user(
        form_data.username,  # Using username field for email
        form_data.password
    )
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(user.id), "email": user.email},
        expires_delta=access_token_expires
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "expires_in": settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60
    }


@router.get("/me", response_model=UserDetail)
async def get_current_user_info(
    current_user: User = Depends(get_current_user)
) -> Any:
    """
    Get current user information.
    
    Requires valid authentication token.
    """
    return current_user


@router.put("/me", response_model=UserDetail)
async def update_current_user(
    user_update: UserUpdate,
    current_user: User = Depends(get_current_user),
    user_service: UserService = Depends(get_user_service)
) -> Any:
    """
    Update current user information.
    
    Requires valid authentication token.
    """
    try:
        updated_user = await user_service.update_user(
            current_user.id, 
            user_update
        )
        
        if not updated_user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        
        return updated_user
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.post("/change-password")
async def change_password(
    password_data: PasswordChange,
    current_user: User = Depends(get_current_user),
    user_service: UserService = Depends(get_user_service)
) -> Any:
    """
    Change current user password.
    
    Requires current password for verification.
    """
    success = await user_service.change_password(
        current_user.id,
        password_data.current_password,
        password_data.new_password
    )
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Current password is incorrect"
        )
    
    return {"message": "Password changed successfully"}


@router.post("/refresh", response_model=Token)
async def refresh_token(
    current_user: User = Depends(get_current_user)
) -> Any:
    """
    Refresh access token.
    
    Returns a new access token for the authenticated user.
    """
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(current_user.id), "email": current_user.email},
        expires_delta=access_token_expires
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "expires_in": settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60
    }


@router.post("/logout")
async def logout() -> Any:
    """
    Logout user.
    
    Note: Since we're using stateless JWT tokens, logout is handled client-side
    by removing the token. In production, consider implementing token blacklisting.
    """
    return {"message": "Successfully logged out"}