import sqlalchemy
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse 
from ..models import Microservice ,Team ,Scorecard ,MicroserviceScoreCard
from ..schemas import MicroserviceCreate, MicroserviceUpdate ,MicroserviceInDBBase , TeamInDBBase ,ScoreCardInDBBase
from .base import CRUDBase
from typing import List
from sqlalchemy.sql import func
from starlette.exceptions import HTTPException




class CRUDMicroservice(CRUDBase[Microservice, MicroserviceCreate, MicroserviceUpdate ]):
    def __init__(self, db_session: Session):
        super(CRUDMicroservice, self).__init__(Microservice, db_session)
        #self.teamService= CRUDTeam(db_session)
        #self.scoreCardService= CRUDMicroserviceScoreCard(db_session)
        
    def getByTeamId(self, teamId: str):
        return self.db_session.query(Microservice).filter(Microservice.teamId == teamId).all()

    def getByTeamIdAndCode(self, teamId: str, code: str):
        return self.db_session.query(Microservice).filter(Microservice.teamId == teamId, Microservice.code == code).first()
    
    #get all with team
    #def getAllByTeamName(self) -> list[MicroserviceInDBBase]:
    #    result = (
    #    self.db_session.query(Microservice.id, Microservice.name, Microservice.description, Microservice.code, Team.name.label("team_name"))
    #    .join(Team, Microservice.teamId == Team.id).all()
    #    )
    #    return result
    
    def getAllServicesByTeamName(self) -> list[MicroserviceInDBBase]:
        
        microservices = self.list()
        services = []
        
        for microservice in microservices:
        # Get the related team for each microservice
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
       
#create one
    def create_service(db: Session, service: MicroserviceCreate):
   
        db_service = service(name=service.name, description=service.description,teamid=service.teamId)
        db.add(db_service)
        db.commit()
        db.refresh(db_service)

      