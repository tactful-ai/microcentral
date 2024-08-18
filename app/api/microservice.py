from fastapi import APIRouter ,Depends,HTTPException
from app.schemas import MicroserviceInDBBase , MicroserviceCreate , MicroserviceTeamScorecardBase ,MicroserviceCreateApi, MicroserviceScoreCardCreate
from app.crud import CRUDMicroservice, CRUDMicroserviceTeamScorecard ,CRUDTeam, CRUDScoreCard, CRUDMicroserviceScoreCard
from typing import List
from app import dependencies 
from pydantic import BaseModel, Field


class Value(BaseModel):
    value: int | bool | float | str = Field(..., title="Value", description="Value of the metric")

router = APIRouter()

@router.get("/", response_model=List[MicroserviceInDBBase])
#@router.get("/Dashboard", response_model=List[MicroserviceInDBBase])
def get_all_services(microServices: CRUDMicroservice = Depends(dependencies.getMicroservicesCrud)):
    return microServices.getAllServicesByTeamName()

@router.get("/{service_id}", response_model=MicroserviceInDBBase)
async def getOne_service(service_id: int, microServices: CRUDMicroservice = Depends(dependencies.getMicroservicesCrud)):
    service = microServices.getByServiceIdWithTeamName(service_id)
    if service is None:
        raise HTTPException(status_code=404, detail="Service not found")
    return service

@router.get("/scorecards/{service_id}", response_model=MicroserviceTeamScorecardBase)
async def getmicroservice_with_teamAndScorecards(service_id: int, microServicesteamScorecard: CRUDMicroserviceTeamScorecard = Depends(dependencies.getMicroserviceTeamScoreCardCrud)):
    service = microServicesteamScorecard.getByServiceIdWithTeamAndSCOREDetails(service_id)
    if service is None:
        raise HTTPException(status_code=404, detail="Service not found")
    return service

@router.post("/create/", response_model= None)
def create_microservice(newmicroservice: MicroserviceCreateApi, 
                        microservice: CRUDMicroservice = Depends(dependencies.getMicroservicesCrud),
                        teamservice: CRUDTeam = Depends(dependencies.getTeamsCrud),
                        servicescorecard: CRUDMicroserviceScoreCard = Depends(dependencies.getMicroserviceScoreCardsCrud),
                        scorecard: CRUDScoreCard = Depends(dependencies.getScoreCardsCrud)):
    try:
        teamservice.get(newmicroservice.teamid)
        scorecard.getByScoreCradIds(newmicroservice.scorecardids)                                         
    except Exception as x:
        error_message = 'Team Id was not found'
        print(error_message)
    
    try:
        scorecard.getByScoreCradIds(newmicroservice.scorecardids)                                         
    except Exception as x:
        error_message = 'ScoreCard Id was not found'
        print(error_message)
        
    created_microservice = microservice.create(MicroserviceCreate(name=newmicroservice.name,
                                            description=newmicroservice.description,
                                            teamId=newmicroservice.teamId,
                                            code=newmicroservice.name.replace(" ","_")))
    
     # Create microservice scorecard associations
    for scorecard in newmicroservice.scorecardids:
        servicescorecard.create(MicroserviceScoreCardCreate(
            microserviceId=created_microservice.id,scoreCardId=scorecard))
            
    return created_microservice
    
