from fastapi import APIRouter ,Depends,HTTPException ,status
from app.schemas import MicroserviceInDBBase , MicroserviceCreate , MicroserviceTeamScorecardBase ,MicroserviceCreateApi, MicroserviceScoreCardCreate , MicroserviceUpdate, MicroserviceScoreCardUpdate
from app.crud import CRUDMicroservice, CRUDMicroserviceTeamScorecard ,CRUDTeam, CRUDScoreCard, CRUDMicroserviceScoreCard
from typing import List
from app import dependencies 
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
import re

class Value(BaseModel):
    value: int | bool | float | str = Field(..., title="Value", description="Value of the service")

router = APIRouter()

def format_code(name):
    code = name.strip()
    code = code.replace(" ", "-")
    code = re.sub(r'-+', '-', code)
    return code

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

@router.get("/serviceDetails/{service_id}", response_model=MicroserviceTeamScorecardBase)
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
    
    microservice.check_service_name_exists(newmicroservice.name)
    formatted_code = format_code(newmicroservice.name)
    existing_microservice = microservice.get_by_code(formatted_code)
    if existing_microservice:
        raise HTTPException(status_code=400, detail="Code already exists")
    
    if not newmicroservice.name:
        raise HTTPException(status_code=400, detail="Name cannot be empty")
    
    if len(newmicroservice.name) < 3:
        raise HTTPException(status_code=400, detail="Name must be at least 3 characters long")
    
    if not newmicroservice.description :
        raise HTTPException(status_code=400, detail="Description cannot be empty")
    
    if len(newmicroservice.description) > 500:
        raise HTTPException(status_code=400, detail="Description cannot exceed 500 characters")
 
    if newmicroservice.teamId:
        try:
            teamobj = teamservice.get(newmicroservice.teamId)
            if teamobj is None:
                raise HTTPException(status_code=404, detail="Team not found")
        except Exception as x:
            error_message = 'Team Id was not found'
            raise HTTPException(status_code=404, detail=error_message)
    else:
        pass
    
    if newmicroservice.scorecardids:
        for scorecardid in newmicroservice.scorecardids:
            try:
                scorecard_obj = scorecard.get(scorecardid)
                if scorecard_obj is None:
                    raise HTTPException(status_code=404, detail=f"ScoreCard of ID: {scorecardid} was not found")
            except Exception as x:
                error_message = f'ScoreCard of ID: {scorecardid} was not found'
                raise HTTPException(status_code=404, detail=error_message)

    created_microservice = microservice.create(MicroserviceCreate(name=newmicroservice.name,
                                            description=newmicroservice.description,
                                            teamId=newmicroservice.teamId,
                                            code=formatted_code))
    
   
    if newmicroservice.scorecardids is not None:
        for scorecardid in newmicroservice.scorecardids:
            try:
                scorecard_obj = scorecard.get(scorecardid)
                if scorecard_obj is None:
                    raise HTTPException(status_code=404, detail=f"ScoreCard of ID: {scorecardid} was not found")
                
                servicescorecard.create(MicroserviceScoreCardCreate(
                    microserviceId=created_microservice.id,
                    scoreCardId=scorecardid
                ))
            except Exception as x:
                error_message = f"Failed to create relationship for ScoreCard ID: {scorecardid}. Reason: {str(x)}"
                raise HTTPException(status_code=400, detail=error_message)
            
            
    return created_microservice
    
    
    
    #update operation
@router.put("/update/{servise_id}", response_model= None)
def update_microservice(microservice_id: int,updatemicroservice: MicroserviceCreateApi, 
                        microservice: CRUDMicroservice = Depends(dependencies.getMicroservicesCrud),
                        teamservice: CRUDTeam = Depends(dependencies.getTeamsCrud),
                        servicescorecard: CRUDMicroserviceScoreCard = Depends(dependencies.getMicroserviceScoreCardsCrud),
                        scorecard: CRUDScoreCard = Depends(dependencies.getScoreCardsCrud)):
    
    if not updatemicroservice.name:
        raise HTTPException(status_code=400, detail="Name cannot be empty")
    
    if len(updatemicroservice.name) < 3:
        raise HTTPException(status_code=400, detail="Name must be at least 3 characters long")

    if not updatemicroservice.description :
        raise HTTPException(status_code=400, detail="Description cannot be empty")

    if len(updatemicroservice.description) > 500:
        raise HTTPException(status_code=400, detail="Description cannot exceed 500 characters")
 
    try:
        teamobj = teamservice.get(updatemicroservice.teamId)
        if teamobj is None:
            raise HTTPException(status_code=404, detail="Not Found") 
    except Exception as x:
        error_message = 'Team Id was not found'
        raise HTTPException(status_code=404, detail=error_message)
    for scorecardid in updatemicroservice.scorecardids:
        try:
            scorecard.get(scorecardid)
        except Exception as x:
            error_message = f'ScoreCard of ID: {scorecardid} was not found'
            raise HTTPException(status_code=404, detail=error_message)
        
    
    formatted_code = format_code(updatemicroservice.name)
    updated_microservice = microservice.update(microservice_id, MicroserviceUpdate(
        name=updatemicroservice.name,
        description=updatemicroservice.description,
        teamId=updatemicroservice.teamId,
        code=formatted_code
    ))
    
    servicescorecard.deleteByServiceId(microservice_id)
   
    for scorcardid in updatemicroservice.scorecardids:
        servicescorecard.create(MicroserviceScoreCardCreate(microserviceId=microservice_id,scoreCardId=scorcardid))

    return updated_microservice


@router.delete("/delete/{microservice_id}")
def delete_microservice(
    microservice_id: int,
    microservice: CRUDMicroservice = Depends(dependencies.getMicroservicesCrud),
    servicescorecard: CRUDMicroserviceScoreCard = Depends(dependencies.getMicroserviceScoreCardsCrud)):
   
    try:
        microservice.delete(microservice_id)
    except Exception:
        error_message = "Can't delete Microservice"
        raise HTTPException(status_code=404, detail="Microservice not found")
    try:
        servicescorecard.deleteByServiceId(microservice_id)
    except Exception:
        error_message = "Can't delete Microservice ScoreCard"
        raise HTTPException(status_code=404, detail="Can't delete Microservice ScoreCard")

    
    return {"message": "Microservice and associated scorecards successfully deleted"}
