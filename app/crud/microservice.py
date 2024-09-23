from sqlalchemy.orm import Session
from fastapi import status
from ..models import Microservice ,Team
from ..schemas import MicroserviceCreate, MicroserviceUpdate ,MicroserviceInDBBase
from .base import CRUDBase
from typing import List
from sqlalchemy.sql import func
from app.api.exceptions import HTTPResponseCustomized

class CRUDMicroservice(CRUDBase[Microservice, MicroserviceCreate, MicroserviceUpdate]):
    def __init__(self, db_session: Session):
        super(CRUDMicroservice, self).__init__(Microservice, db_session)

    def getByTeamId(self, teamId: str):
        return self.db_session.query(Microservice).filter(Microservice.teamId == teamId).all()

    def getByTeamIdAndCode(self, teamId: str, code: str):
        return self.db_session.query(Microservice).filter(Microservice.teamId == teamId, Microservice.code == code).first()
    
    def getByServiceId(self, serviceID: int) -> Microservice:
        return self.db_session.query(Microservice).filter(Microservice.id == serviceID).first()
    
    def getByServiceIds(self, serviceID: list[int]) -> list[Microservice]:
        return self.db_session.query(Microservice).filter(Microservice.id.in_(serviceID)).all()

    
    def getAllServicesWithTeamName(self) -> list[MicroserviceInDBBase]:
        
        microservices = self.list()
        services = []
        
        for microservice in microservices:
            team = self.db_session.query(Team).filter(Team.id == microservice.teamId).first()
            
            service = MicroserviceInDBBase(
                id=microservice.id,
                name=microservice.name,
                description=microservice.description,
                code=microservice.code,
                team_name=team.name if team else None,
            )
            services.append(service)
        return services

    #get one with team
    def getByServiceIdWithTeam(self , service_id:int):
        result = (
        self.db_session.query(Microservice.id, Microservice.name, Microservice.description, Microservice.code, Team.name.label("team_name"))
        .filter(Microservice.id == service_id)
        .first()
        )
        return result

    def get_by_code (self , code:str):
        service = self.db_session.query(Microservice).filter(Microservice.code == code).first()
        return service
    
    def getByCodeReturnIDs (self , code:str):
        return self.db_session.query(Microservice).filter(Microservice.code == code).first().id()


    def check_service_name_exists(self, name: str):
        service = self.db_session.query(Microservice).filter(Microservice.name == name).first()
        if service:
            raise HTTPResponseCustomized(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="service name is aready existed"
            )
