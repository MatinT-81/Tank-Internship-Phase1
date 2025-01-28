from sqlmodel import  Field, Relationship

from app.schemas.users import UserBase
from app.models import Author


class User(UserBase, table=True):
    __tablename__ = "users"
    id: int | None = Field(default=None, primary_key=True)
    password: str

    author: "Author" | None = Relationship(back_populates="user")