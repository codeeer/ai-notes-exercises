"""
User service layer for business logic.
Handles complex operations and business rules.
"""
from datetime import datetime
from typing import List, Optional

from sqlalchemy import and_, func, or_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

from app.core.security import hash_password, verify_password
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate


class UserService:
    """Service class for user-related business logic."""
    
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def get_user_by_id(self, user_id: int) -> Optional[User]:
        """Get user by ID (excluding soft deleted)."""
        result = await self.db.execute(
            select(User).where(
                and_(User.id == user_id, User.deleted_at.is_(None))
            )
        )
        return result.scalar_one_or_none()
    
    async def get_user_by_email(self, email: str) -> Optional[User]:
        """Get user by email (excluding soft deleted)."""
        result = await self.db.execute(
            select(User).where(
                and_(User.email == email, User.deleted_at.is_(None))
            )
        )
        return result.scalar_one_or_none()
    
    async def get_user_by_username(self, username: str) -> Optional[User]:
        """Get user by username (excluding soft deleted)."""
        result = await self.db.execute(
            select(User).where(
                and_(User.username == username, User.deleted_at.is_(None))
            )
        )
        return result.scalar_one_or_none()
    
    async def get_users(
        self, 
        skip: int = 0, 
        limit: int = 20,
        search: Optional[str] = None,
        is_active: Optional[bool] = None
    ) -> tuple[List[User], int]:
        """
        Get paginated list of users with optional filtering.
        
        Returns:
            Tuple of (users_list, total_count)
        """
        # Base query (exclude soft deleted)
        query = select(User).where(User.deleted_at.is_(None))
        count_query = select(func.count(User.id)).where(User.deleted_at.is_(None))
        
        # Apply filters
        if search:
            search_filter = or_(
                User.email.ilike(f"%{search}%"),
                User.username.ilike(f"%{search}%"),
                User.full_name.ilike(f"%{search}%")
            )
            query = query.where(search_filter)
            count_query = count_query.where(search_filter)
        
        if is_active is not None:
            query = query.where(User.is_active == is_active)
            count_query = count_query.where(User.is_active == is_active)
        
        # Get total count
        total_result = await self.db.execute(count_query)
        total = total_result.scalar()
        
        # Apply pagination and ordering
        query = query.order_by(User.created_at.desc()).offset(skip).limit(limit)
        
        # Execute query
        result = await self.db.execute(query)
        users = result.scalars().all()
        
        return list(users), total
    
    async def create_user(self, user_data: UserCreate) -> User:
        """Create new user with business validation."""
        # Check if email already exists
        existing_user = await self.get_user_by_email(user_data.email)
        if existing_user:
            raise ValueError("Email already registered")
        
        # Check if username already exists (if provided)
        if user_data.username:
            existing_username = await self.get_user_by_username(user_data.username)
            if existing_username:
                raise ValueError("Username already taken")
        
        # Hash password
        hashed_password = hash_password(user_data.password)
        
        # Create user
        db_user = User(
            email=user_data.email,
            username=user_data.username,
            full_name=user_data.full_name,
            bio=user_data.bio,
            phone=user_data.phone,
            hashed_password=hashed_password,
            is_active=True,
            is_verified=False,  # Email verification required
        )
        
        self.db.add(db_user)
        await self.db.commit()
        await self.db.refresh(db_user)
        
        return db_user
    
    async def update_user(self, user_id: int, user_data: UserUpdate) -> Optional[User]:
        """Update user with business validation."""
        user = await self.get_user_by_id(user_id)
        if not user:
            return None
        
        # Check email uniqueness (if changed)
        if user_data.email and user_data.email != user.email:
            existing_email = await self.get_user_by_email(user_data.email)
            if existing_email:
                raise ValueError("Email already registered")
        
        # Check username uniqueness (if changed)
        if user_data.username and user_data.username != user.username:
            existing_username = await self.get_user_by_username(user_data.username)
            if existing_username:
                raise ValueError("Username already taken")
        
        # Update fields
        update_data = user_data.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(user, field, value)
        
        user.updated_at = datetime.utcnow()
        
        await self.db.commit()
        await self.db.refresh(user)
        
        return user
    
    async def delete_user(self, user_id: int) -> bool:
        """Soft delete user."""
        user = await self.get_user_by_id(user_id)
        if not user:
            return False
        
        user.soft_delete()
        await self.db.commit()
        
        return True
    
    async def authenticate_user(self, email: str, password: str) -> Optional[User]:
        """Authenticate user with email and password."""
        user = await self.get_user_by_email(email)
        if not user:
            return None
        
        if not user.is_active:
            return None
        
        if not verify_password(password, user.hashed_password):
            return None
        
        # Update login tracking
        user.last_login = datetime.utcnow()
        user.login_count += 1
        await self.db.commit()
        
        return user
    
    async def change_password(
        self, 
        user_id: int, 
        current_password: str, 
        new_password: str
    ) -> bool:
        """Change user password with current password verification."""
        user = await self.get_user_by_id(user_id)
        if not user:
            return False
        
        # Verify current password
        if not verify_password(current_password, user.hashed_password):
            return False
        
        # Update password
        user.hashed_password = hash_password(new_password)
        user.updated_at = datetime.utcnow()
        
        await self.db.commit()
        
        return True
    
    async def activate_user(self, user_id: int) -> bool:
        """Activate user account."""
        user = await self.get_user_by_id(user_id)
        if not user:
            return False
        
        user.is_active = True
        user.is_verified = True
        user.updated_at = datetime.utcnow()
        
        await self.db.commit()
        
        return True
    
    async def deactivate_user(self, user_id: int) -> bool:
        """Deactivate user account."""
        user = await self.get_user_by_id(user_id)
        if not user:
            return False
        
        user.is_active = False
        user.updated_at = datetime.utcnow()
        
        await self.db.commit()
        
        return True
    
    async def get_user_stats(self) -> dict:
        """Get user statistics."""
        # Total users
        total_result = await self.db.execute(
            select(func.count(User.id)).where(User.deleted_at.is_(None))
        )
        total_users = total_result.scalar()
        
        # Active users
        active_result = await self.db.execute(
            select(func.count(User.id)).where(
                and_(User.deleted_at.is_(None), User.is_active == True)
            )
        )
        active_users = active_result.scalar()
        
        # Verified users
        verified_result = await self.db.execute(
            select(func.count(User.id)).where(
                and_(User.deleted_at.is_(None), User.is_verified == True)
            )
        )
        verified_users = verified_result.scalar()
        
        # Users created today
        today = datetime.utcnow().date()
        today_result = await self.db.execute(
            select(func.count(User.id)).where(
                and_(
                    User.deleted_at.is_(None),
                    func.date(User.created_at) == today
                )
            )
        )
        users_today = today_result.scalar()
        
        return {
            "total_users": total_users,
            "active_users": active_users,
            "verified_users": verified_users,
            "users_created_today": users_today,
            "verification_rate": round((verified_users / total_users * 100), 2) if total_users > 0 else 0,
            "activation_rate": round((active_users / total_users * 100), 2) if total_users > 0 else 0,
        }