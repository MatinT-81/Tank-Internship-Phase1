from sqlmodel import SQLModel, Field

from typing import List

from app.models.genres import Genre


class BookBase(SQLModel):
    title: str
    price: float
    units: int
    description: str | None = Field(default=None)

class BookCreate(BookBase):
    ISBN: str
    genre_id: int
    author_id: List[int]

class BookRead(BookBase):
    id: int
    ISBN: str
    genre: Genre
    genre_id: int
    authors: List[int] = []
    
class BookUpdate(BookBase):
    ISBN: str
    