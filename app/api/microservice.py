from fastapi import APIRouter ,Depends,HTTPException
from app.schemas import MicroserviceInDBBase , MicroserviceCreate ,MicroserviceTeamScorecardBase
from app.crud import CRUDMicroservice ,CRUDMicroserviceTeamScorecard
from typing import List
from app import dependencies 
from pydantic import BaseModel, Field


class Value(BaseModel):
    value: int | bool | float | str = Field(..., title="Value", description="Value of the metric")

router = APIRouter()

#@router.get("/", response_model=List[MicroserviceInDBBase])
##@router.get("/Dashboard", response_model=List[MicroserviceInDBBase])
#def get_all_services(microServices: CRUDMicroservice = Depends(dependencies.getMicroservicesCrud)):
#    return microServices.getAllServicesByTeamName()

#@router.get("/{service_id}", response_model=MicroserviceInDBBase)
#async def getOne_service(service_id: int, microServices: CRUDMicroservice = Depends(dependencies.getMicroservicesCrud)):
#    service = microServices.getByServiceIdWithTeamName(service_id)
#    if service is None:
#        raise HTTPException(status_code=404, detail="Service not found")
#    return service

@router.get("/scorecards/{service_id}", response_model=MicroserviceTeamScorecardBase)
async def getmicroservice_with_teamAndScorecards(service_id: int, microServicesteamScorecard: CRUDMicroserviceTeamScorecard = Depends(dependencies.getMicroserviceTeamScoreCardCrud)):
    service = microServicesteamScorecard.getByServiceIdWithTeamAndSCOREDetails(service_id)
    if service is None:
        raise HTTPException(status_code=404, detail="Service not found")
    return service

#@router.post("/Create/", response_model=MicroserviceCreate)
#def create_microservice(newmicroservice: MicroserviceCreate ,microservice: CRUDMicroservice = Depends(dependencies.getMicroservicesCrud)):
#    created_microservice = microservice.create(newmicroservice)
    
#    return created_microservice
    


