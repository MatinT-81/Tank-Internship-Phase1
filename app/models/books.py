from sqlmodel import  Field, Relationship

from typing import List, Optional

from app.schemas.books import BookBase
from app.models.links import BookAuthorLink
from app.models.genres import Genre


class Book(BookBase, table=True):
    __tablename__ = "books"
    id: int | None = Field(default=None, primary_key=True)
    ISBN: str

    authors: List["Author"] = Relationship(back_populates="books", link_model=BookAuthorLink)
    
    genre_id: Optional[int] = Field(foreign_key="genres.id", ondelete="CASCADE")
    genre: Optional[Genre] = Relationship(back_populates="books")