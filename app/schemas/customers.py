from datetime import datetime
from sqlmodel import SQLModel

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

class CustomerCreate(CustomerBase):
    password: str

class CustomerRead(CustomerBase):
    id: int
    wallet_money_amount: float

class CustomerUpdate(CustomerBase):
    password: str | None = None
    wallet_money_amount: float | None = None
