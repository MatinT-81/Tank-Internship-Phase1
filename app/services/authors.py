from sqlmodel import select

from fastapi import HTTPException, status

from app.models import Author, User, City, Book
from app.models.links import BookAuthorLink
from app.dependecies import SessionDep

class AuthorService:
    async def get_all_authors(self, offset: int, limit: int, session: SessionDep):
        authors = await session.exec(select(Author).offset(offset).limit(limit))
        authors = authors.all()
        if not authors:
            raise HTTPException(detail="No authors found", status_code=status.HTTP_404_NOT_FOUND)
        return authors

    async def get_author(self, author_id: int, session: SessionDep):
        author = await session.get(Author, author_id)
        if not author:
            raise HTTPException(detail="Author not found", status_code=status.HTTP_404_NOT_FOUND)
        return author

    async def create_author(self, author: Author, session: SessionDep):
        errors = {}
        user = await session.get(User, author.user_id)
        if not user:
            # raise HTTPException(detail="User not found", status_code=status.HTTP_404_NOT_FOUND)
            errors["user_id"] = "User not found"
        
        city = await session.get(City, author.city_id)
        if not city:
            # raise HTTPException(detail="City not found", status_code=status.HTTP_404_NOT_FOUND)
            errors["city_id"] = "City not found"
        
        for book_id in author.books:
            book = await session.get(BookAuthorLink, book_id)
            if not book:
                # raise HTTPException(detail=f"Book with id {book_id} not found", status_code=status.HTTP_404_NOT_FOUND)
                errors["book_id"] = f"Book with id {book_id} not found"
        
        if errors:
            raise HTTPException(detail=errors, status_code=status.HTTP_404_NOT_FOUND)
        
        session.add(author)
        await session.commit()
        await session.refresh(author)
        return author

    async def update_author(self, author_id: int, author_data: dict, session: SessionDep):
        author = await session.get(Author, author_id)
        if not author:
            raise HTTPException(detail="Author not found", status_code=status.HTTP_404_NOT_FOUND)
        
        errors = {}
        user = await session.get(User, author.user_id)
        if not user:
            # raise HTTPException(detail="User not found", status_code=status.HTTP_404_NOT_FOUND)
            errors["user_id"] = "User not found"
        
        city = await session.get(City, author.city_id)
        if not city:
            # raise HTTPException(detail="City not found", status_code=status.HTTP_404_NOT_FOUND)
            errors["city_id"] = "City not found"
        
        for book_id in author.books:
            book = await session.get(BookAuthorLink, book_id)
            if not book:
                # raise HTTPException(detail=f"Book with id {book_id} not found", status_code=status.HTTP_404_NOT_FOUND)
                errors["book_id"] = f"Book with id {book_id} not found"
        
        if errors:
            raise HTTPException(detail=errors, status_code=status.HTTP_404_NOT_FOUND)
        
        for key, value in author_data.items():
            setattr(author, key, value)
        session.add(author)
        await session.commit()
        await session.refresh(author)
        return author

    async def delete_author(self, author_id: int, session: SessionDep):
        author = await session.get(Author, author_id)
        if not author:
            raise HTTPException(detail="Author not found", status_code=status.HTTP_404_NOT_FOUND)
        await session.delete(author)
        await session.commit()
        return {"detail": "Author deleted"}

async def get_author_service() -> AuthorService:
    return AuthorService()