import sqlalchemy
from sqlalchemy.orm import Session
from ..models import Microservice
from ..schemas import MicroserviceTeamScorecardBase, team, scoreCard
from .base import CRUDBase
from typing import List
from sqlalchemy.sql import func
from starlette.exceptions import HTTPException
from . import CRUDTeam, CRUDMicroserviceScoreCard, CRUDScoreCard ,CRUDMicroservice



class CRUDMicroserviceTeamScorecard:
    def __init__(self, db_session: Session):
        self.microsService =CRUDMicroservice(db_session)
        self.teamService= CRUDTeam(db_session)
        self.scoreCardService= CRUDMicroserviceScoreCard(db_session) 
        self.scoreCard = CRUDScoreCard(db_session) 

    # Get all with scorecard and team
    def getByServiceIdWithTeamAndSCOREDetails(self, service_id: int)-> MicroserviceTeamScorecardBase:
    
        microservice = self.microsService.get(service_id)
       
        if not microservice:
            raise Exception(f"Microservice with id {service_id} not found")
        
        
        teamobject = self.teamService.get(microservice.teamId)  

        scorecardIds = self.scoreCardService.getByServiceId(microservice.id)
        scorecards = []
        
        for sc_id in scorecardIds:
            scorecard = self.scoreCard.get(sc_id.scoreCardId)
            if scorecard:
                scorecards.append(scorecard)
        
        
        service = MicroserviceTeamScorecardBase(
            id=microservice.id,
            name=microservice.name,
            description=microservice.description,
            code=microservice.code,
            team=team.TeamBase(id=teamobject.id, name=teamobject.name) if team else None,  
            scorecards=[scoreCard.ScoreCardInDBBase(id=sc.id, name=sc.name, description=sc.description) for sc in scorecards]
        )
        return service