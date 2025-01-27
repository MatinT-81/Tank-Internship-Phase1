from typing import Annotated
from fastapi import Depends
from sqlmodel.ext.asyncio.session import AsyncSession


from .database import engine


async def get_session():
    async with AsyncSession(engine) as session:
        yield session
SessionDep = Annotated[AsyncSession, Depends(get_session)]