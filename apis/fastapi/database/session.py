from corelib.config import get_settings
from database.models.base import BaseModel
from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from typing import Annotated

settings = get_settings()

connect_args = {"check_same_thread": False}

engine = create_engine(
    settings.db_connection_string,
    connect_args
)

def get_session():
    with Session(engine) as session:
        yield session

def ensure_database_created():
    BaseModel.metadata.create_all(engine)

SessionDep = Annotated[Session, Depends(get_session)]