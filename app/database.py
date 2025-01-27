from sqlmodel import create_engine, SQLModel
from .config import settings

from sqlalchemy.ext.asyncio import create_async_engine


DATABASE_URL = f"postgresql+asyncpg://{settings.db_username}:{settings.db_password}@{settings.db_host}:{settings.db_port}/{settings.db_name}"

# engine = create_engine(DATABASE_URL, echo=True)

engine = create_async_engine(DATABASE_URL, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
