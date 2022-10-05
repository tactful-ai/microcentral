
from sqlalchemy.orm import Session

from ...core.models import Microservice
from ...core.schemas.microservice import MicroserviceCreate, MicroserviceUpdate
from .base import BaseService


class MicroservicesService(BaseService[Microservice, MicroserviceCreate, MicroserviceUpdate]):
    def __init__(self, db_session: Session):
        super(MicroservicesService, self).__init__(Microservice, db_session)

    def getByTeamId(self, teamId: str):
        return self.db_session.query(Microservice).filter(Microservice.teamId == teamId).all()

    def getByTeamIdAndCode(self, teamId: str, code: str):
        return self.db_session.query(Microservice).filter(Microservice.teamId == teamId, Microservice.code == code).first()
