
from app.core.models import Microservice
from app.core.schemas.microservice import (MicroserviceCreate,
                                           MicroserviceUpdate)
from sqlalchemy.orm import Session

from .base import BaseService


class MicroservicesService(BaseService[Microservice, MicroserviceCreate, MicroserviceUpdate]):
    def __init__(self, db_session: Session):
        super(MicroservicesService, self).__init__(Microservice, db_session)
