from typing import Annotated, Dict, List

from sqlmodel import select
from fastapi import (
    APIRouter , HTTPException , status,
    Query
    )

from app.models.users import User
from app.schemas.users import *
from app.dependecies import SessionDep


router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, session: SessionDep) -> UserRead:

    user = User.model_validate(user)
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user


@router.get("/", response_model=List[UserRead])
async def read_users(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100) -> List[UserRead]:
        users = await session.exec(select(User).offset(offset).limit(limit))
        users = users.all()
        if not users:
            raise HTTPException(detail="No users found" , status_code=status.HTTP_404_NOT_FOUND)
        return users


@router.get("/{user_id}", response_model=UserRead)
async def read_user(user_id: int, session: SessionDep) -> UserRead:
    user = await session.get(User, user_id)
    if not user:
        raise HTTPException(detail="User not found" , status_code=status.HTTP_404_NOT_FOUND)
    return user


@router.patch("/{user_id}", response_model=UserRead)
async def update_user(user_id: int, user: UserUpdate, session: SessionDep) -> UserRead:
    db_user = await session.get(User, user_id)
    if not db_user:
        raise HTTPException(detail="User not found" , status_code=status.HTTP_404_NOT_FOUND)
    user_data = user.model_dump(exclude_unset=True)
    for key, value in user_data.items():
        setattr(db_user, key, value)
    session.add(db_user)
    await session.commit()
    await session.refresh(db_user)
    return db_user


@router.delete("/{user_id}")
async def delete_user(user_id: int, session: SessionDep) -> Dict[str, str]:
    user = await session.get(User, user_id)
    if not user:
        raise HTTPException(detail="User not found", status_code=status.HTTP_404_NOT_FOUND)
    await session.delete(user)
    await session.commit()
    return {"detail": "User deleted"}
