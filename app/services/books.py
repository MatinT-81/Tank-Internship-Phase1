from sqlmodel import select

from fastapi import HTTPException, status

from app.models.books import Book
from app.dependecies import SessionDep

class BookService:
    async def get_all_books(self, offset: int, limit: int, session: SessionDep):
        books = await session.exec(select(Book).offset(offset).limit(limit))
        books = books.all()
        if not books:
            raise HTTPException(detail="No books found", status_code=status.HTTP_404_NOT_FOUND)
        return books

    async def get_book(self, book_id: int, session: SessionDep):
        book = await session.get(Book, book_id)
        if not book:
            raise HTTPException(detail="Book not found", status_code=status.HTTP_404_NOT_FOUND)
        return book

    async def create_book(self, book: Book, session: SessionDep):
        session.add(book)
        await session.commit()
        await session.refresh(book)
        return book

    async def update_book(self, book_id: int, book_data: dict, session: SessionDep):
        book = await session.get(Book, book_id)
        if not book:
            raise HTTPException(detail="Book not found", status_code=status.HTTP_404_NOT_FOUND)
        for key, value in book_data.items():
            setattr(book, key, value)
        session.add(book)
        await session.commit()
        await session.refresh(book)
        return book

    async def delete_book(self, book_id: int, session: SessionDep):
        book = await session.get(Book, book_id)
        if not book:
            raise HTTPException(detail="Book not found", status_code=status.HTTP_404_NOT_FOUND)
        await session.delete(book)
        await session.commit()
        return {"detail": "Book deleted"}

async def get_book_service() -> BookService:
    return BookService()