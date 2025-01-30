from sqlmodel import SQLModel

from pydantic import validator

from typing import List

from app.schemas.books import BookRead
from app.models.cities import City


class AuthorBase(SQLModel):
    first_name: str
    last_name: str

class AuthorCreate(AuthorBase):
    bank_account_number: str
    goodreads_url: str
    user_id: int
    city_id: int
    book_id: List[int]

    @validator('bank_account_number')
    def validate_bank_account_number(cls, v):
        if len(v) != 16 and not v.isdigit():
            raise ValueError("Bank account number must be 16 digits")
        return v

class AuthorRead(AuthorBase):
    id: int
    bank_account_number: str
    goodreads_url: str
    user_id: int
    books: List[BookRead] = []  # remember have picture for api response 
    city: City
    city_id: int

class AuthorUpdate(AuthorBase):
    bank_account_number: str | None = None
    goodreads_url: str | None = None

    @validator('bank_account_number')
    def validate_bank_account_number(cls, v):
        if len(v) != 16 and not v.isdigit():
            raise ValueError("Bank account number must be 16 digits")
        return v