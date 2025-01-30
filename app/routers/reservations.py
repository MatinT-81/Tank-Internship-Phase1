from typing import Annotated, Dict, List

from fastapi import APIRouter, status, Query, Depends

from app.models.reservations import Reservation
from app.schemas.reservations import ReservationCreate, ReservationRead, ReservationUpdate
from app.dependecies import SessionDep
from app.services.reservations import ReservationService, get_reservation_service

router = APIRouter(prefix="/reservations", tags=["Reservations"])

@router.post("/", response_model=ReservationRead, status_code=status.HTTP_201_CREATED)
async def create_reservation(reservation: ReservationCreate, session: SessionDep) -> ReservationRead:
    reservation = Reservation.model_validate(reservation)
    reservation_service = await get_reservation_service()
    return await reservation_service.create_reservation(reservation, session)

@router.get("/", response_model=List[ReservationRead])
async def read_all_reservations(
    session: SessionDep,
    offset: int = 0,
    reservation_service: ReservationService = Depends(get_reservation_service),
    limit: Annotated[int, Query(le=100)] = 100) -> List[ReservationRead]:
    return await reservation_service.get_all_reservations(offset, limit, session)

@router.get("/{reservation_id}", response_model=ReservationRead)
async def read_reservation(reservation_id: int, session: SessionDep) -> ReservationRead:
    reservation_service = await get_reservation_service()
    return await reservation_service.get_reservation(reservation_id, session)

@router.patch("/{reservation_id}", response_model=ReservationRead)
async def update_reservation(reservation_id: int, reservation: ReservationUpdate, session: SessionDep) -> ReservationRead:
    reservation_service = await get_reservation_service()
    reservation_data = reservation.model_dump(exclude_unset=True)
    return await reservation_service.update_reservation(reservation_id, reservation_data, session)

@router.delete("/{reservation_id}")
async def delete_reservation(reservation_id: int, session: SessionDep) -> Dict[str, str]:
    reservation_service = await get_reservation_service()
    return await reservation_service.delete_reservation(reservation_id, session)