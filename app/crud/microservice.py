
from sqlalchemy.orm import Session

from ..models import Microservice ,Team
from ..schemas import MicroserviceCreate, MicroserviceUpdate ,MicroserviceInDBBase
from .base import CRUDBase
from typing import List


class CRUDMicroservice(CRUDBase[Microservice, MicroserviceCreate, MicroserviceUpdate]):
    def __init__(self, db_session: Session):
        super(CRUDMicroservice, self).__init__(Microservice, db_session)

    def getByTeamId(self, teamId: str):
        return self.db_session.query(Microservice).filter(Microservice.teamId == teamId).all()

    def getByTeamIdAndCode(self, teamId: str, code: str):
        return self.db_session.query(Microservice).filter(Microservice.teamId == teamId, Microservice.code == code).first()
    
    def getAllByTeamName(self) -> list[MicroserviceInDBBase]:
        result = (
        self.db_session.query(Microservice.id, Microservice.name, Microservice.description, Microservice.code, Team.name.label("team_name"))
        .join(Team, Microservice.teamId == Team.id).all()
        )
        return result
   
    def getAllByServiceIdWithTeamName(self , service_id:int):
        result = (
        self.db_session.query(Microservice.id, Microservice.name, Microservice.description, Microservice.code, Team.name.label("team_name"))
        .join(Team, Microservice.teamId == Team.id)
        .filter(Microservice.id == service_id)
        .first()
        )
        return result
    
    
    
    
    