from typing import Annotated, Dict, List

from fastapi import APIRouter, status, Query, Depends

from app.models.customers import Customer
from app.schemas.customers import CustomerCreate, CustomerRead, CustomerUpdate
from app.dependecies import SessionDep
from app.services.customers import CustomerService, get_customer_service

router = APIRouter(prefix="/customers", tags=["Customers"])

@router.post("/", response_model=CustomerRead, status_code=status.HTTP_201_CREATED)
async def create_customer(customer: CustomerCreate, session: SessionDep) -> CustomerRead:
    customer = Customer.model_validate(customer)
    customer_service = await get_customer_service()
    return await customer_service.create_customer(customer, session)

@router.get("/", response_model=List[CustomerRead])
async def read_all_customers(
    session: SessionDep,
    offset: int = 0,
    customer_service: CustomerService = Depends(get_customer_service),
    limit: Annotated[int, Query(le=100)] = 100) -> List[CustomerRead]:
    return await customer_service.get_all_customers(offset, limit, session)

@router.get("/{customer_id}", response_model=CustomerRead)
async def read_customer(customer_id: int, session: SessionDep) -> CustomerRead:
    customer_service = await get_customer_service()
    return await customer_service.get_customer(customer_id, session)

@router.patch("/{customer_id}", response_model=CustomerRead)
async def update_customer(customer_id: int, customer: CustomerUpdate, session: SessionDep) -> CustomerRead:
    customer_service = await get_customer_service()
    customer_data = customer.model_dump(exclude_unset=True)
    return await customer_service.update_customer(customer_id, customer_data, session)

@router.delete("/{customer_id}")
async def delete_customer(customer_id: int, session: SessionDep) -> Dict[str, str]:
    customer_service = await get_customer_service()
    return await customer_service.delete_customer(customer_id, session)