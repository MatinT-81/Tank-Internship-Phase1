from sqlmodel import SQLModel, Field

from pydantic import validator

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

    @validator("ISBN")
    def validate_ISBN(cls, v):
        if len(v) != 13:
            raise ValueError("ISBN must be 13 characters")
        return v
    
    @validator("units")
    def validate_units(cls, v):
        if v < 0:
            raise ValueError("Units must be greater than 0")
        return v

class BookRead(BookBase):
    id: int
    ISBN: str
    genre: Genre
    genre_id: int
    authors: List[int] = []
    
class BookUpdate(BookBase):
    ISBN: str
    