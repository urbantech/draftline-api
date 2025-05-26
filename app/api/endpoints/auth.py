from datetime import timedelta
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.core import security
from app.core.config import settings

router = APIRouter()

@router.post("/login/access-token", response_model=schemas.Token)
def login_access_token(
    db: Session = Depends(deps.get_db), form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """
    OAuth2 compatible token login, get an access token for future requests.
    
    Args:
        db: Database session
        form_data: OAuth2 form with username (email) and password
        
    Returns:
        JWT access token and token type
        
    Raises:
        HTTPException: If authentication fails or user is inactive
    """
    # Try to authenticate user with provided credentials
    user = crud.user.authenticate(
        db, email=form_data.username, password=form_data.password
    )
    
    # Handle authentication failure
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Check if user account is active
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="Account is disabled"
        )
    
    # Generate access token with configured expiration
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    token = security.create_access_token(
        user.id, expires_delta=access_token_expires
    )
    
    # Return token data
    return {
        "access_token": token,
        "token_type": "bearer",
    }

@router.get("/me", response_model=schemas.User)
def read_current_user(current_user: models.User = Depends(deps.get_current_active_user)) -> Any:
    """
    Get current user information based on the provided JWT token.
    
    Args:
        current_user: Current user model (from JWT token)
        
    Returns:
        Current authenticated user information
    """
    return current_user

@router.post("/register", response_model=schemas.User, status_code=status.HTTP_201_CREATED)
def create_user_signup(
    *,
    db: Session = Depends(deps.get_db),
    user_in: schemas.UserCreate,
) -> Any:
    """
    Register a new user without requiring authentication.
    
    Args:
        db: Database session
        user_in: User creation data including email, password, and full name
        
    Returns:
        Newly created user data (without password)
        
    Raises:
        HTTPException: If a user with the same email already exists
    """
    # Check if user with this email already exists
    user = crud.user.get_user_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="The user with this email already exists.",
        )
    
    # Create new user in the database
    user = crud.user.create_user(db, user=user_in)
    return user
