from pydantic import BaseModel, EmailStr
from typing import Optional
from enum import Enum
from datetime import datetime

class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    user_id: int
    created_at: datetime
    class Config:
        orm_mode = True

class PortfolioBase(BaseModel):
    name: str

class PortfolioCreate(PortfolioBase):
    user_id: int

class Portfolio(PortfolioBase):
    portfolio_id: int
    user_id: int
    class Config:
        orm_mode = True
