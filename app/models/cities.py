from sqlmodel import SQLModel, Field, Relationship

from typing import List


class City(SQLModel, table=True):
    __tablename__ = "cities"
    id: int | None = Field(default=None, primary_key=True)
    name: str

    authors: List["Author"] = Relationship(back_populates="city", cascade_delete=True)