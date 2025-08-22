from pydantic import BaseModel, EmailStr
from typing import List

class UserBase(BaseModel):
    id: int
    email: EmailStr
    full_name: str
    class Config: orm_mode = True

class AccountBase(BaseModel):
    id: int
    balance: float
    class Config: orm_mode = True

class PaymentBase(BaseModel):
    transaction_id: str
    amount: float
    class Config: orm_mode = True

class UserDetail(UserBase):
    accounts: List[AccountBase] = []
    payments: List[PaymentBase] = []

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class WebhookRequest(BaseModel):
    transaction_id: str
    user_id: int
    account_id: int
    amount: float
    signature: str
