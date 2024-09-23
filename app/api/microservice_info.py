from fastapi import APIRouter, Depends
from app.schemas import  MicroserviceInfoBase
from app.crud import CRUDMicroserviceInfo
from typing import List
from app import dependencies
from pydantic import BaseModel, Field
from .exceptions import HTTPResponseCustomized


class Value(BaseModel):
    value: int | bool | float | str = Field(
        ..., title="Value", description="Value of the serviceinfo")


router = APIRouter()


@router.get("/{service_id}", response_model=MicroserviceInfoBase)
async def getmicroservice_info(service_id: int, microServiceinfo: CRUDMicroserviceInfo = Depends(dependencies.getMicroserviceInfoCrud)):
    service = microServiceinfo.getServiceInfo(service_id)
    if service is None:
        raise HTTPResponseCustomized(status_code=404, detail="Service not found")
    return service