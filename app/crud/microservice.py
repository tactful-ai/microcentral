import sqlalchemy
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse 
from ..models import Microservice ,Team ,Scorecard ,MicroserviceScoreCard
from ..schemas import MicroserviceCreate, MicroserviceUpdate ,MicroserviceInDBBase , TeamInDBBase ,ScoreCardInDBBase
from .base import CRUDBase
from typing import List
from sqlalchemy.sql import func
from starlette.exceptions import HTTPException


class CRUDMicroservice(CRUDBase[Microservice, MicroserviceCreate, MicroserviceUpdate]):
    def __init__(self, db_session: Session):
        super(CRUDMicroservice, self).__init__(Microservice, db_session)

    def getByTeamId(self, teamId: str):
        return self.db_session.query(Microservice).filter(Microservice.teamId == teamId).all()

    def getByTeamIdAndCode(self, teamId: str, code: str):
        return self.db_session.query(Microservice).filter(Microservice.teamId == teamId, Microservice.code == code).first()

   
    
    def getAllServicesByTeamName(self) -> list[MicroserviceInDBBase]:
        
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
    def getByServiceIdWithTeamName(self , service_id:int):
        result = (
        self.db_session.query(Microservice.id, Microservice.name, Microservice.description, Microservice.code, Team.name.label("team_name"))
        .join(Team, Microservice.teamId == Team.id)
        .filter(Microservice.id == service_id)
        .first()
        )
        return result
      
   
    #def delete(self, microservice_id: int):
    #    session = self.db_session()
    #    microservice = session.query(Microservice).filter(id=microservice_id).first()
    #    if not microservice:
    #        raise HTTPException(status_code=404, detail="Microservice not found")
        
    #    session.delete(microservice)
    #    session.commit() 

      