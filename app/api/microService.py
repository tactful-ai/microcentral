from fastapi import APIRouter ,Depends,HTTPException
from app.schemas import MicroserviceInDBBase 
from app.crud import CRUDMicroservice 
from typing import List
from app import dependencies 
from pydantic import BaseModel, Field


class Value(BaseModel):
    value: int | bool | float | str = Field(..., title="Value", description="Value of the metric")

router = APIRouter()

@router.get("/", response_model=List[MicroserviceInDBBase])
#@router.get("/Dashboard", response_model=List[MicroserviceInDBBase])
def get_all_services(microServices: CRUDMicroservice = Depends(dependencies.getMicroservicesCrud)):
    return microServices.getAllByTeamName()

@router.get("/{service_id}", response_model=MicroserviceInDBBase)
#@router.get("/Dashboard", response_model=List[MicroserviceInDBBase])
async def get_all_services(service_id: int, microServices: CRUDMicroservice = Depends(dependencies.getMicroservicesCrud)):
    service = microServices.getAllByServiceIdWithTeamName(service_id)
    if service is None:
        raise HTTPException(status_code=404, detail="Service not found")
    return service
