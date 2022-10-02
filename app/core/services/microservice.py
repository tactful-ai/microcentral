
from sqlalchemy.orm import Session

from ...core.models import Microservice
from ...core.schemas.microservice import MicroserviceCreate, MicroserviceUpdate
from .base import BaseService


class MicroservicesService(BaseService[Microservice, MicroserviceCreate, MicroserviceUpdate]):
    def __init__(self, db_session: Session):
        super(MicroservicesService, self).__init__(Microservice, db_session)
