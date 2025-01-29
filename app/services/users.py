from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select

from fastapi import HTTPException , status

from app.models.users import User


class UserService():  
    async def read_users(self,offset, limit, db :AsyncSession ):
        users = await db.exec(select(User).offset(offset).limit(limit))
        users = users.all()
        if not users:
            raise HTTPException(detail="No users found" , status_code=status.HTTP_404_NOT_FOUND)
        return users

    async def read_user(self, user_id: int, db: AsyncSession):
        user = await db.get(User, user_id)
        if not user:
            raise HTTPException(detail="User not found", status_code=status.HTTP_404_NOT_FOUND)
        return user

    async def create_user(self, user: User, db: AsyncSession):
        db.add(user)
        await db.commit()
        await db.refresh(user)
        return user

    async def update_user(self, user_id: int, user_data: dict, db: AsyncSession):
        user = await db.get(User, user_id)
        if not user:
            raise HTTPException(detail="User not found", status_code=status.HTTP_404_NOT_FOUND)
        for key, value in user_data.items():
            setattr(user, key, value)
        db.add(user)
        await db.commit()
        await db.refresh(user)
        return user

    async def delete_user(self, user_id: int, db: AsyncSession):
        user = await db.get(User, user_id)
        if not user:
            raise HTTPException(detail="User not found", status_code=status.HTTP_404_NOT_FOUND)
        await db.delete(user)
        await db.commit()
        return {"detail": "User deleted"}

async def get_user_service() -> UserService:
    return UserService()
