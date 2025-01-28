from sqlmodel import SQLModel
from pydantic import EmailStr
from enum import Enum


class UserRole(str, Enum):
    SYSTEM_ADMIN = "System Admins"
    CUSTOMER = "Customers"
    AUTHOR = "Authors"

class UserBase(SQLModel):
    username: str 
    first_name: str
    last_name: str
    phone_num: str
    email: EmailStr
    user_role: UserRole

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int
    author_id: int | None = None

class UserUpdate(UserBase):
    password: str