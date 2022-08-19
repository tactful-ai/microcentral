from app.database import get_session
from fastapi import Depends
from sqlalchemy.orm import Session

from .service import UsersService


def get_users_service(db_session: Session = Depends(get_session)) -> UsersService:
    return UsersService(db_session)
