# ---------------------------------------packages----------------------------------------------
from sqlmodel import SQLModel, Field
from pydantic import EmailStr
from enum import Enum

# ---------------------------------------UserModel----------------------------------------------
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

class Users(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    password: str

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int

class UserUpdate(UserBase):
    password: str


