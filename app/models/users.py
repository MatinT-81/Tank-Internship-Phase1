from sqlmodel import  Field, Relationship

from app.schemas.users import UserBase
from app.models import Author


class User(UserBase, table=True):
    __tablename__ = "users"
    id: int | None = Field(default=None, primary_key=True)
    password: str

    author: "Author" = Relationship(back_populates="user", cascade_delete=True)

    customer: "Customer" = Relationship(back_populates="user", cascade_delete=True)
