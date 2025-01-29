from sqlmodel import SQLModel, Field


class BookBase(SQLModel):
    title: str
    price: float
    units: int
    description: str | None = Field(default=None)
    
class BookCreate(BookBase):
    ISBN: str

class BookRead(BookBase):
    id: int
    ISBN: str

class BookUpdate(BookBase):
    ISBN: str