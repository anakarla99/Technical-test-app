from datetime import datetime

from pydantic import BaseModel, validator
from typing import Optional

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class UserCreate(BaseModel):
    email: str
    password: str

class UserRead(BaseModel):
    id: int
    email: str
    is_active: bool
    
    class Config:
        from_attributes = True

class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    
    @validator('status')
    def status_must_be_valid(cls, v):
        if v and v not in ["pendiente", "completada"]:
            raise ValueError('Estado debe ser "pendiente" o "completada"')
        return v


class TodoRead(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: str
    created_at: datetime
    user_id: int