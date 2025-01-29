from typing import Annotated, Dict, List

from fastapi import (
    APIRouter, status,
    Query, Depends
    )

from app.models.users import * 
from app.schemas.users import *
from app.dependecies import SessionDep
from app.services.users import UserService, get_user_service


router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, session: SessionDep) -> UserRead:
    user = User.model_validate(user)
    client_service = await get_user_service()
    return await client_service.create_user(user, session)

@router.get("/", response_model=List[UserRead])
async def read_users(
    session: SessionDep,
    offset: int = 0,
    client_service: UserService = Depends(get_user_service),
    limit: Annotated[int, Query(le=100)] = 100) -> List[UserRead]:
    return await client_service.read_users(offset, limit, session)

@router.get("/{user_id}", response_model=UserRead)
async def read_user(user_id: int, session: SessionDep) -> UserRead:
    client_service = await get_user_service()
    return await client_service.read_user(user_id, session)

@router.patch("/{user_id}", response_model=UserRead)
async def update_user(user_id: int, user: UserUpdate, session: SessionDep) -> UserRead:
    client_service = await get_user_service()
    user_data = user.model_dump(exclude_unset=True)
    return await client_service.update_user(user_id, user_data, session)

@router.delete("/{user_id}")
async def delete_user(user_id: int, session: SessionDep) -> Dict[str, str]:
    client_service = await get_user_service()
    return await client_service.delete_user(user_id, session)