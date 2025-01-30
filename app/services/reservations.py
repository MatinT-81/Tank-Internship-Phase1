from sqlmodel import select

from fastapi import HTTPException, status

from app.models import Reservation, Book, Customer
from app.dependecies import SessionDep

class ReservationService:
    async def get_all_reservations(self, offset: int, limit: int, session: SessionDep):
        reservations = await session.exec(select(Reservation).offset(offset).limit(limit))
        reservations = reservations.all()
        if not reservations:
            raise HTTPException(detail="No reservations found", status_code=status.HTTP_404_NOT_FOUND)
        return reservations

    async def get_reservation(self, reservation_id: int, session: SessionDep):
        reservation = await session.get(Reservation, reservation_id)
        if not reservation:
            raise HTTPException(detail="Reservation not found", status_code=status.HTTP_404_NOT_FOUND)
        return reservation

    async def create_reservation(self, reservation: Reservation, session: SessionDep):
        errors = {}
        book = await session.get(Book, reservation.book_id)
        if not book:
            errors["book_id"] = "Book not found"

        customer = await session.get(Customer, reservation.customer_id)
        if not customer:
            errors["customer_id"] = "Customer not found"
        
        if errors:
            raise HTTPException(detail=errors, status_code=status.HTTP_404_NOT_FOUND)

        session.add(reservation)
        await session.commit()
        await session.refresh(reservation)
        return reservation

    async def update_reservation(self, reservation_id: int, reservation_data: dict, session: SessionDep):
        reservation = await session.get(Reservation, reservation_id)
        if not reservation:
            raise HTTPException(detail="Reservation not found", status_code=status.HTTP_404_NOT_FOUND)
        
        errors = {}
        book = await session.get(Book, reservation.book_id)
        if not book:
            errors["book_id"] = "Book not found"

        customer = await session.get(Customer, reservation.customer_id)
        if not customer:
            errors["customer_id"] = "Customer not found"
        
        if errors:
            raise HTTPException(detail=errors, status_code=status.HTTP_404_NOT_FOUND)
        
        for key, value in reservation_data.items():
            setattr(reservation, key, value)
        session.add(reservation)
        await session.commit()
        await session.refresh(reservation)
        return reservation

    async def delete_reservation(self, reservation_id: int, session: SessionDep):
        reservation = await session.get(Reservation, reservation_id)
        if not reservation:
            raise HTTPException(detail="Reservation not found", status_code=status.HTTP_404_NOT_FOUND)
        await session.delete(reservation)
        await session.commit()
        return {"detail": "Reservation deleted"}

async def get_reservation_service() -> ReservationService:
    return ReservationService()