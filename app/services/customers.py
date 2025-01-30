from sqlmodel import select

from fastapi import HTTPException, status

from app.models import Customer, User
from app.dependecies import SessionDep

class CustomerService:
    async def get_all_customers(self, offset: int, limit: int, session: SessionDep):
        customers = await session.exec(select(Customer).offset(offset).limit(limit))
        customers = customers.all()
        if not customers:
            raise HTTPException(detail="No customers found", status_code=status.HTTP_404_NOT_FOUND)
        return customers

    async def get_customer(self, customer_id: int, session: SessionDep):
        customer = await session.get(Customer, customer_id)
        if not customer:
            raise HTTPException(detail="Customer not found", status_code=status.HTTP_404_NOT_FOUND)
        return customer

    async def create_customer(self, customer: Customer, session: SessionDep):
        user = await session.get(User, customer.user_id)
        if not user:
            raise HTTPException(detail="User not found", status_code=status.HTTP_404_NOT_FOUND)

        session.add(customer)
        await session.commit()
        await session.refresh(customer)
        return customer

    async def update_customer(self, customer_id: int, customer_data: dict, session: SessionDep):
        customer = await session.get(Customer, customer_id)
        if not customer:
            raise HTTPException(detail="Customer not found", status_code=status.HTTP_404_NOT_FOUND)
        for key, value in customer_data.items():
            setattr(customer, key, value)
        session.add(customer)
        await session.commit()
        await session.refresh(customer)
        return customer

    async def delete_customer(self, customer_id: int, session: SessionDep):
        customer = await session.get(Customer, customer_id)
        if not customer:
            raise HTTPException(detail="Customer not found", status_code=status.HTTP_404_NOT_FOUND)
        await session.delete(customer)
        await session.commit()
        return {"detail": "Customer deleted"}

async def get_customer_service() -> CustomerService:
    return CustomerService()