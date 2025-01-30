from datetime import datetime
from sqlmodel import SQLModel

from pydantic import validator

from enum import Enum

class CostomerSubModel(str, Enum):
    FREE = "Free"
    PLUS = "Plus"
    PREMUIM = "Premuim"

class CustomerBase(SQLModel):
    username: str
    first_name: str
    last_name: str
    subscription_model: CostomerSubModel
    subscription_end_time: datetime | None = None

    @validator("username")
    def validate_username(cls, v):
        if 'admin' in v:
            raise ValueError("'admin' can't be in username")
        return v

class CustomerCreate(CustomerBase):
    user_id: int
    password: str

class CustomerRead(CustomerBase):
    id: int
    wallet_money_amount: float

class CustomerUpdate(CustomerBase):
    password: str | None = None
    wallet_money_amount: float | None = None
