from sqlmodel import  Field, Relationship

from typing import List

from app.schemas.authors import AuthorBase

from app.models.links import BookAuthorLink
from app.models import User
from app.models import Book


class Author(AuthorBase, table=True):
    __tablename__ = "authors"
    id: int | None = Field(default=None, primary_key=True)
    bank_account_number: str
    goodreads_url: str

    user_id: int = Field(foreign_key="users.id")
    user: "User" = Relationship(back_populates="author")

    books: List["Book"] = Relationship(back_populates="authors", link_model=BookAuthorLink)