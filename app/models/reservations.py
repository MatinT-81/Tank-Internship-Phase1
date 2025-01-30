from sqlmodel import Field, Relationship
from datetime import datetime
from typing import List, Optional

from app.schemas.reservations import ReservationBase


class Reservation(ReservationBase, table=True):
    __tablename__ = "reservations"
    id: int | None = Field(default=None, primary_key=True)

    book_id: int = Field(foreign_key="books.id", ondelete="CASCADE")
    book: Optional["Book"] = Relationship(back_populates="reservation")
    
    customer_id: int = Field(foreign_key="customers.id", ondelete="CASCADE")
    customer: Optional["Customer"] = Relationship(back_populates="reservation")