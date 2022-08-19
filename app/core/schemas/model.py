from pydantic import BaseModel, EmailStr
from pydantic.types import UUID4


class User(BaseModel):
    id: UUID4
    email: EmailStr
    hashed_password: str
    is_active: bool

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    hashed_password: str


class UserUpdate(BaseModel):
    email: EmailStr
    hashed_password: str
    is_active: bool = None

    class Config:
        orm_mode = True

