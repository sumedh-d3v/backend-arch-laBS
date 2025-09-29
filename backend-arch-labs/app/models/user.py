from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    email: EmailStr

class UserUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=1, max_length=100)

class User(BaseModel):
    id: int
    name: str
    email: EmailStr
