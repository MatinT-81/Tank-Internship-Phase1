from sqlmodel import select

from fastapi import HTTPException, status

from app.models import Author
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
        session.add(author)
        await session.commit()
        await session.refresh(author)
        return author

    async def update_author(self, author_id: int, author_data: dict, session: SessionDep):
        author = await session.get(Author, author_id)
        if not author:
            raise HTTPException(detail="Author not found", status_code=status.HTTP_404_NOT_FOUND)
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