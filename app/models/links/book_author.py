from sqlmodel import Field, SQLModel


class BookAuthorLink(SQLModel, table=True):
    book_id: int | None = Field(default=None, foreign_key="books.id", primary_key=True)
    author_id: int | None = Field(default=None, foreign_key="authors.id", primary_key=True)
