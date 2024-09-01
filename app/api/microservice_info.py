from fastapi import APIRouter, Depends
from app.schemas import MicroserviceInDBBase, ScoreCardBase , MicroserviceInfoBase
from app.crud import CRUDMicroservice, CRUDMicroserviceInfo, CRUDTeam, CRUDScoreCard, CRUDMicroserviceScoreCard
from typing import List
from app import dependencies
from pydantic import BaseModel, Field
#from sqlalchemy.orm import Session
from .exceptions import ExceptionCustom
import re

class Value(BaseModel):
    value: int | bool | float | str = Field(
        ..., title="Value", description="Value of the serviceinfo")


router = APIRouter()


#def format_code(name):
#    code = re.sub(r'\s+', '-', name.strip())
#    return code

@router.get("/{service_id}", response_model=MicroserviceInfoBase)
async def getmicroservice_info(service_id: int, microServiceinfo: CRUDMicroserviceInfo = Depends(dependencies.getMicroserviceInfoCrud)):
    service = microServiceinfo.getServiceInfo(
        service_id)
    if service is None:
        raise ExceptionCustom(status_code=404, detail="Service not found")
    return service