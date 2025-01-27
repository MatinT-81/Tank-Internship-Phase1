# ---------------------------------------packages----------------------------------------------
from typing import Annotated
from sqlmodel import select
from fastapi import (
    FastAPI , HTTPException , status,
    Query, Body
    )

from .database import create_db_and_tables, SessionDep
from .models import *

from typing import Dict, List

# ---------------------------------------base code----------------------------------------------
app = FastAPI()

@app.on_event("startup")
async def on_startup():
    create_db_and_tables()

# ---------------------------------------User----------------------------------------------

@app.post("/user/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, session: SessionDep) -> UserRead:
    user = Users.model_validate(user)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@app.get("/users/", response_model=List[UserRead])
def read_users(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100) -> List[UserRead]:
        users = session.exec(select(Users).offset(offset).limit(limit)).all()
        if not users:
            raise HTTPException(detail="No users found" , status_code=status.HTTP_404_NOT_FOUND)
        return users

@app.get("/users/{user_id}", response_model=UserRead)
def read_user(user_id: int, session: SessionDep) -> UserRead:
    user = session.get(Users, user_id)
    if not user:
        raise HTTPException(detail="User not found" , status_code=status.HTTP_404_NOT_FOUND)
    return user

@app.patch("/users/{user_id}", response_model=UserRead)
def update_user(user_id: int, user: UserUpdate, session: SessionDep) -> UserRead:
    db_user = session.get(Users, user_id)
    if not db_user:
        raise HTTPException(detail="User not found" , status_code=status.HTTP_404_NOT_FOUND)
    user_data = user.model_dump(exclude_unset=True)
    for key, value in user_data.items():
        setattr(db_user, key, value)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


@app.delete("/users/{user_id}")
def delete_user(user_id: int, session: SessionDep) -> Dict[str, str]:
    user = session.get(Users, user_id)
    if not user:
        raise HTTPException(detail="User not found", status_code=status.HTTP_404_NOT_FOUND)
    session.delete(user)
    session.commit()
    return {"detail": "User deleted"}

@app.delete("/users/all/", response_model=Dict[str, str])
def delete_all_users(session: SessionDep, confirmation: str = Body(...)) -> Dict[str, str]:
    confirmation = confirmation.strip()
    if confirmation != "I know what I'm doing!":
        raise HTTPException(status_code=400, detail="Invalid confirmation text")
    users = session.exec(select(Users)).all()
    if not users:
        raise HTTPException(status_code=404, detail="No users found")
    for user in users:
        session.delete(user)
    session.commit()
    return {"detail": "All users deleted"}
