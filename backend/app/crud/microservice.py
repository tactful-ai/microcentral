
from sqlalchemy.orm import Session

from ..models import Microservice
from ..schemas.microservice import MicroserviceCreate, MicroserviceUpdate
from .base import CRUDBase


class CRUDMicroservice(CRUDBase[Microservice, MicroserviceCreate, MicroserviceUpdate]):
    def __init__(self, db_session: Session):
        super(CRUDMicroservice, self).__init__(Microservice, db_session)

    def getByTeamId(self, teamId: str):
        return self.db_session.query(Microservice).filter(Microservice.teamId == teamId).all()

    def getByTeamIdAndCode(self, teamId: str, code: str):
        return self.db_session.query(Microservice).filter(Microservice.teamId == teamId, Microservice.code == code).first()
