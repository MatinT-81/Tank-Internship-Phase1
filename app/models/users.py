from sqlmodel import  Field
from app.schemas.users import UserBase


class User(UserBase, table=True):
    __tablename__ = "users"
    id: int | None = Field(default=None, primary_key=True)
    password: str




