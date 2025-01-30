from sqlmodel import SQLModel

from pydantic import validator

from datetime import datetime


class ReservationBase(SQLModel):
    start_time: datetime
    end_time: datetime
    price: float

class ReservationCreate(ReservationBase):
    book_id: int
    customer_id: int

    @validator("start_time")
    def validate_start_time(cls, v):
        if v < datetime.now():
            raise ValueError("Start time cannot be in the past")
        return v
    
    @validator("end_time")
    def validate_end_time(cls, v, values):
        if "start_time" in values and v < values["start_time"]:
            raise ValueError("End time cannot be before start time")
        return v

class ReservationRead(ReservationBase):
    id: int
    book_id: int
    customer_id: int

class ReservationUpdate(ReservationBase):
    start_time: datetime | None = None
    end_time: datetime | None = None
    price: float | None = None
