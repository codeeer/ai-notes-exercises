from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from . import crud, models, schemas
from .database import SessionLocal, engine, get_db

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(
    title="User Management API",
    description="A simple User Management API built with FastAPI and PostgreSQL",
    version="1.0.0"
)

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to User Management API"}

# Health check
@app.get("/health")
def health_check():
    return {"status": "healthy"}

# GET /api/users - Get all users
@app.get("/api/users", response_model=List[schemas.User])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

# GET /api/users/{user_id} - Get user by ID
@app.get("/api/users/{user_id}", response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# GET /api/users/email/{email} - Get user by email
@app.get("/api/users/email/{email}", response_model=schemas.User)
def get_user_by_email(email: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# GET /api/users/search?name=xxx - Search users by name
@app.get("/api/users/search", response_model=List[schemas.User])
def search_users(name: str, db: Session = Depends(get_db)):
    users = crud.search_users_by_name(db, name=name)
    return users

# POST /api/users - Create new user
@app.post("/api/users", response_model=schemas.User, status_code=201)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Check if user with email already exists
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

# PUT /api/users/{user_id} - Update user
@app.put("/api/users/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    db_user = crud.update_user(db, user_id=user_id, user=user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# DELETE /api/users/{user_id} - Delete user
@app.delete("/api/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    success = crud.delete_user(db, user_id=user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}

# GET /api/users/count - Get user count
@app.get("/api/users/count")
def get_user_count(db: Session = Depends(get_db)):
    count = crud.get_user_count(db)
    return {"count": count}

# Error handlers
@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    return {"error": "Internal server error", "detail": str(exc)}