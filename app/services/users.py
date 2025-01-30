from sqlmodel import select

from fastapi import HTTPException, status

from app.models.users import User
from app.dependecies import SessionDep

class UserService:
    async def get_all_users(self, offset: int, limit: int, session: SessionDep):
        users = await session.exec(select(User).offset(offset).limit(limit))
        users = users.all()
        if not users:
            raise HTTPException(detail="No users found", status_code=status.HTTP_404_NOT_FOUND)
        return users

    async def get_user(self, user_id: int, session: SessionDep):
        user = await session.get(User, user_id)
        if not user:
            raise HTTPException(detail="User not found", status_code=status.HTTP_404_NOT_FOUND)
        return user

    async def create_user(self, user: User, session: SessionDep):
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user

    async def update_user(self, user_id: int, user_data: dict, session: SessionDep):
        user = await session.get(User, user_id)
        if not user:
            raise HTTPException(detail="User not found", status_code=status.HTTP_404_NOT_FOUND)
        for key, value in user_data.items():
            setattr(user, key, value)
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user

    async def delete_user(self, user_id: int, session: SessionDep):
        user = await session.get(User, user_id)
        if not user:
            raise HTTPException(detail="User not found", status_code=status.HTTP_404_NOT_FOUND)
        await session.delete(user)
        await session.commit()
        return {"detail": "User deleted"}

async def get_user_service() -> UserService:
    return UserService()