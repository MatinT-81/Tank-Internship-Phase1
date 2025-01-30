from typing import Annotated, Dict, List

from fastapi import APIRouter, status, Query, Depends

from app.models import Book
from app.schemas.books import BookCreate, BookRead, BookUpdate
from app.dependecies import SessionDep
from app.services.books import BookService, get_book_service

router = APIRouter(prefix="/books", tags=["Books"])

@router.post("/", response_model=BookRead, status_code=status.HTTP_201_CREATED)
async def create_book(book: BookCreate, session: SessionDep) -> BookRead:
    book = Book.model_validate(book)
    book_service = await get_book_service()
    return await book_service.create_book(book, session)

@router.get("/", response_model=List[BookRead])
async def read_all_books(
    session: SessionDep,
    offset: int = 0,
    book_service: BookService = Depends(get_book_service),
    limit: Annotated[int, Query(le=100)] = 100) -> List[BookRead]:
    return await book_service.get_all_books(offset, limit, session)

@router.get("/{book_id}", response_model=BookRead)
async def read_book(book_id: int, session: SessionDep) -> BookRead:
    book_service = await get_book_service()
    return await book_service.get_book(book_id, session)

@router.patch("/{book_id}", response_model=BookRead)
async def update_book(book_id: int, book: BookUpdate, session: SessionDep) -> BookRead:
    book_service = await get_book_service()
    book_data = book.model_dump(exclude_unset=True)
    return await book_service.update_book(book_id, book_data, session)

@router.delete("/{book_id}")
async def delete_book(book_id: int, session: SessionDep) -> Dict[str, str]:
    book_service = await get_book_service()
    return await book_service.delete_book(book_id, session)