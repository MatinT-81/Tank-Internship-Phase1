from typing import Annotated, Dict, List

from fastapi import APIRouter, status, Query, Depends

from app.models import Author
from app.schemas.authors import AuthorCreate, AuthorRead, AuthorUpdate
from app.dependecies import SessionDep
from app.services.authors import AuthorService, get_author_service

router = APIRouter(prefix="/authors", tags=["Authors"])

@router.post("/", response_model=AuthorRead, status_code=status.HTTP_201_CREATED)
async def create_author(author: AuthorCreate, session: SessionDep) -> AuthorRead:
    author = Author.model_validate(author)
    author_service = await get_author_service()
    return await author_service.create_author(author, session)

@router.get("/", response_model=List[AuthorRead])
async def read_all_authors(
    session: SessionDep,
    offset: int = 0,
    author_service: AuthorService = Depends(get_author_service),
    limit: Annotated[int, Query(le=100)] = 100) -> List[AuthorRead]:
    return await author_service.get_all_authors(offset, limit, session)

@router.get("/{author_id}", response_model=AuthorRead)
async def read_author(author_id: int, session: SessionDep) -> AuthorRead:
    author_service = await get_author_service()
    return await author_service.get_author(author_id, session)

@router.patch("/{author_id}", response_model=AuthorRead)
async def update_author(author_id: int, author: AuthorUpdate, session: SessionDep) -> AuthorRead:
    author_service = await get_author_service()
    author_data = author.model_dump(exclude_unset=True)
    return await author_service.update_author(author_id, author_data, session)

@router.delete("/{author_id}")
async def delete_author(author_id: int, session: SessionDep) -> Dict[str, str]:
    author_service = await get_author_service()
    return await author_service.delete_author(author_id, session)