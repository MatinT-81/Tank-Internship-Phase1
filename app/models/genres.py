from sqlmodel import SQLModel, Field, Relationship

from typing import List


class Genre(SQLModel, table=True):
    __tablename__ = "genres"
    id: int | None = Field(default=None, primary_key=True)
    name: str

    books: List["Book"] = Relationship(back_populates="genre", cascade_delete=True)
