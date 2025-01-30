from datetime import datetime

from sqlmodel import Field, Relationship

from app.schemas.customers import CustomerBase


class Customer(CustomerBase, table=True):
    __tablename__ = "customers"
    id: int | None = Field(default=None, primary_key=True)
    password: str
    wallet_money_amount: float = Field(default=0.0)
    subscription_end_time: datetime | None = Field(default=None)

    user_id: int | None = Field(default=None, foreign_key="users.id", ondelete="CASCADE")
    user: "User" = Relationship(back_populates="customer")