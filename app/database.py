# ---------------------------------------packages----------------------------------------------
from sqlmodel import create_engine, SQLModel, Session
from typing import Annotated
from fastapi import Depends

from .config import settings

# ---------------------------------------Database----------------------------------------------
DATABASE_URL = f"postgresql://{settings.db_username}:{settings.db_password}@{settings.db_host}:{settings.db_port}/{settings.db_name}"

engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Dependency for create Session
def get_session():
    with Session(engine) as session:
        yield session
SessionDep = Annotated[Session, Depends(get_session)]