import logging
from typing import Any, Dict

from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.core.config import settings
from app.db import base  # noqa: F401

# Make sure all SQL Alchemy models are imported before initializing DB
# Otherwise, SQL Alchemy might fail to initialize relationships properly

def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    # Base.metadata.create_all(bind=engine)

    user = crud.user.get_by_email(db, email=settings.FIRST_SUPERUSER_EMAIL)
    if not user:
        user_in = schemas.UserCreate(
            email=settings.FIRST_SUPERUSER_EMAIL,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            full_name=settings.FIRST_SUPERUSER,
            is_superuser=True,
        )
        user = crud.user.create(db, obj_in=user_in)  # noqa: F841
        logging.info("Initial superuser created")
