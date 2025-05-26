import os
import subprocess
import time
import uvicorn
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from app.core.config import settings
from app.db.base_class import Base
from app.models.user import User  # noqa
from app.core.security import get_password_hash

def setup_db():
    """Setup database if it doesn't exist"""
    engine = create_engine(settings.DATABASE_URL)
    
    if not database_exists(engine.url) and 'sqlite' not in settings.DATABASE_URL:
        create_database(engine.url)
        print(f"Created database: {settings.DATABASE_URL}")

    # Create tables
    Base.metadata.create_all(bind=engine)
    print("Created database tables")

def create_first_superuser():
    """Create a test superuser if defined in env vars"""
    from sqlalchemy.orm import Session
    from app.db.session import SessionLocal
    
    db = SessionLocal()
    try:
        # Check if superuser exists
        user = db.query(User).filter(User.email == settings.FIRST_SUPERUSER_EMAIL).first()
        if not user:
            user_obj = User(
                email=settings.FIRST_SUPERUSER_EMAIL,
                hashed_password=get_password_hash(settings.FIRST_SUPERUSER_PASSWORD),
                full_name=settings.FIRST_SUPERUSER,
                is_superuser=True,
                is_active=True
            )
            db.add(user_obj)
            db.commit()
            print(f"Created first superuser: {settings.FIRST_SUPERUSER_EMAIL}")
    finally:
        db.close()

if __name__ == "__main__":
    print("Setting up database...")
    setup_db()
    
    print("Creating first superuser...")
    create_first_superuser()
    
    print("Starting API server...")
    uvicorn.run("app.main:app", host="0.0.0.0", port=8080, reload=True)
