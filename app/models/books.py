from sqlmodel import  Field, Relationship

from typing import List

from app.schemas.books import BookBase
from app.models.links import BookAuthorLink
from app.models import Author


class Book(BookBase, table=True):
    __tablename__ = "books"
    id: int | None = Field(default=None, primary_key=True)
    ISBN: str

    authors: List["Author"] = Relationship(back_populates="books", link_model=BookAuthorLink)