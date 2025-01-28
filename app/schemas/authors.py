from sqlmodel import SQLModel

from typing import List

from app.schemas.books import BookRead


class AuthorBase(SQLModel):
    city: str

class AuthorCreate(AuthorBase):
    bank_account_number: str
    goodreads_url: str
    user_id: int

class AuthorRead(AuthorBase):
    id: int
    bank_account_number: str
    goodreads_url: str
    user_id: int
    books: List[BookRead] = []  # remember have picture for api response 

class AuthorUpdate(AuthorBase):
    bank_account_number: str
    goodreads_url: str