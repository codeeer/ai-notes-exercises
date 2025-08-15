"""
User management endpoints with CRUD operations.
Comprehensive user management with filtering and pagination.
"""
from typing import Any, Optional

from fastapi import APIRouter, Depends, HTTPException, Query, status

from app.api.dependencies import (
    get_current_superuser,
    get_current_user,
    get_user_service
)
from app.core.config import settings
from app.models.user import User
from app.schemas.user import (
    UserCreate,
    UserDetail,
    UserListResponse,
    UserResponse,
    UserUpdate
)
from app.services.user import UserService

router = APIRouter()


@router.get("/", response_model=UserListResponse)
async def get_users(
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(
        settings.DEFAULT_PAGE_SIZE, 
        ge=1, 
        le=settings.MAX_PAGE_SIZE,
        description="Items per page"
    ),
    search: Optional[str] = Query(None, description="Search in email, username, or full name"),
    is_active: Optional[bool] = Query(None, description="Filter by active status"),
    user_service: UserService = Depends(get_user_service),
    _: User = Depends(get_current_superuser)  # Only superusers can list all users
) -> Any:
    """
    Get paginated list of users.
    
    **Requires superuser privileges.**
    
    - **page**: Page number (starts from 1)
    - **page_size**: Number of users per page
    - **search**: Search term for email, username, or full name
    - **is_active**: Filter by user active status
    """
    skip = (page - 1) * page_size
    
    users, total = await user_service.get_users(
        skip=skip,
        limit=page_size,
        search=search,
        is_active=is_active
    )
    
    total_pages = (total + page_size - 1) // page_size
    
    return {
        "users": users,
        "total": total,
        "page": page,
        "page_size": page_size,
        "total_pages": total_pages
    }


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(
    user_data: UserCreate,
    user_service: UserService = Depends(get_user_service),
    _: User = Depends(get_current_superuser)  # Only superusers can create users
) -> Any:
    """
    Create a new user.
    
    **Requires superuser privileges.**
    
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


@router.get("/{user_id}", response_model=UserDetail)
async def get_user(
    user_id: int,
    user_service: UserService = Depends(get_user_service),
    current_user: User = Depends(get_current_user)
) -> Any:
    """
    Get user by ID.
    
    Users can view their own profile.
    Superusers can view any user profile.
    """
    user = await user_service.get_user_by_id(user_id)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    # Check permissions
    if not current_user.is_superuser and current_user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions"
        )
    
    return user


@router.put("/{user_id}", response_model=UserDetail)
async def update_user(
    user_id: int,
    user_update: UserUpdate,
    user_service: UserService = Depends(get_user_service),
    current_user: User = Depends(get_current_user)
) -> Any:
    """
    Update user by ID.
    
    Users can update their own profile.
    Superusers can update any user profile.
    """
    # Check permissions
    if not current_user.is_superuser and current_user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions"
        )
    
    try:
        updated_user = await user_service.update_user(user_id, user_update)
        
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


@router.delete("/{user_id}")
async def delete_user(
    user_id: int,
    user_service: UserService = Depends(get_user_service),
    current_user: User = Depends(get_current_superuser)  # Only superusers can delete
) -> Any:
    """
    Soft delete user by ID.
    
    **Requires superuser privileges.**
    
    This performs a soft delete - the user is marked as deleted
    but the record remains in the database.
    """
    # Prevent superuser from deleting themselves
    if current_user.id == user_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot delete your own account"
        )
    
    success = await user_service.delete_user(user_id)
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    return {"message": "User deleted successfully"}


@router.post("/{user_id}/activate")
async def activate_user(
    user_id: int,
    user_service: UserService = Depends(get_user_service),
    _: User = Depends(get_current_superuser)  # Only superusers can activate
) -> Any:
    """
    Activate user account.
    
    **Requires superuser privileges.**
    
    Sets user as active and verified.
    """
    success = await user_service.activate_user(user_id)
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    return {"message": "User activated successfully"}


@router.post("/{user_id}/deactivate")
async def deactivate_user(
    user_id: int,
    user_service: UserService = Depends(get_user_service),
    current_user: User = Depends(get_current_superuser)  # Only superusers can deactivate
) -> Any:
    """
    Deactivate user account.
    
    **Requires superuser privileges.**
    
    Sets user as inactive (cannot login).
    """
    # Prevent superuser from deactivating themselves
    if current_user.id == user_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot deactivate your own account"
        )
    
    success = await user_service.deactivate_user(user_id)
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    return {"message": "User deactivated successfully"}


@router.get("/stats/overview")
async def get_user_stats(
    user_service: UserService = Depends(get_user_service),
    _: User = Depends(get_current_superuser)  # Only superusers can view stats
) -> Any:
    """
    Get user statistics overview.
    
    **Requires superuser privileges.**
    
    Returns comprehensive statistics about users including:
    - Total users count
    - Active users count  
    - Verified users count
    - Users created today
    - Verification and activation rates
    """
    stats = await user_service.get_user_stats()
    return stats