from sqlmodel import  Field, Relationship

from typing import List

from app.schemas.books import BookBase
from app.models.links import BookAuthorLink


class Book(BookBase, table=True):
    __tablename__ = "books"
    id: int | None = Field(default=None, primary_key=True)
    ISBN: str

    authors: List["Author"] = Relationship(back_populates="books", link_model=BookAuthorLink)
    
    genre_id: int = Field(foreign_key="genres.id")
    genre: "Genre" = Relationship(back_populates="books")