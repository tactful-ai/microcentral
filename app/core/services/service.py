
from app.core.models import User
from app.core.schemas.model import UserCreate, UserUpdate
from sqlalchemy.orm import Session

from .base import BaseService


class UsersService(BaseService[User, UserCreate, UserUpdate]):
    def __init__(self, db_session: Session):
        super(UsersService, self).__init__(User, db_session)
