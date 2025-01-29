from sqlmodel import SQLModel
from pydantic import EmailStr, validator
from enum import Enum
import re


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

    @validator('phone_num')
    def validate_phone_num(cls, v):
        pattern1 = "^09[\d]{9}$"
        pattern2 = "^\+989[\d]{9}$"
        if not (re.match(pattern1, v) or re.match(pattern2, v)):
            raise ValueError("Phone number is not valid")
        return v

    @validator('username')
    def validate_username(cls, v):
        if 'admin' in v:
            raise ValueError("'admin' can't be in username")
        return v

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int
    author_id: int | None = None

class UserUpdate(UserBase):
    password: str | None = None