from sqlmodel import SQLModel

from datetime import datetime


class ReservationBase(SQLModel):
    start_time: datetime
    end_time: datetime
    price: float

class ReservationCreate(ReservationBase):
    book_id: int
    user_id: int

class ReservationRead(ReservationBase):
    id: int
    book_id: int
    user_id: int

class ReservationUpdate(ReservationBase):
    start_time: datetime | None = None
    end_time: datetime | None = None
    price: float | None = None
