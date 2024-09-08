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
        ..., title="Value", description="Value of the metricinfo")


router = APIRouter()
