from app import dependencies 
from fastapi.exceptions import RequestValidationError
from app.schemas import ServiceMetricCreate, MetricCreate, scoreCard, microserviceScoreCard
from fastapi import APIRouter, Depends, Request, exception_handlers, status, Response, HTTPException
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field
from app.crud import CRUDMetric, CRUDServiceMetric, CRUDMicroserviceScoreCard, CRUDMicroservice
from app import schemas, models, crud
from typing import Any, List
import json
from fastapi.routing import APIRoute
from app.utils.base import format_code

router = APIRouter()

@router.post("/", response_model=schemas.ScoreCard)
def createScoreCard(scoreCard: schemas.ScoreCardCreate, scoreCardCrud: crud.CRUDScoreCard = Depends(dependencies.getScoreCardsCrud)) -> Any:
    scoreCard.code = format_code(scoreCard.name)
    return scoreCardCrud.create(scoreCard)



# I get all the scorecards id then go to microserviceSCORECARD to get all ids of microservices related to one scorecardID
@router.get("/", response_model=List[schemas.ScoreCard])
def getAllScoreCard(scoreCardCrud: crud.CRUDScoreCard = Depends(dependencies.getScoreCardsCrud)):
    scoreCards = scoreCardCrud.list()
    return scoreCards


# Get Single Scorecard by its won ID (NOTE: This is working on the old DB of scorecard 
# DATA of scorecard retreived is : 1- ID 2- Name 3- Descritpion)
@router.get("/{scorecardID}", response_model=schemas.ScoreCard)
def getScoreCard(scorecardID: int, scoreCardCrud: crud.CRUDScoreCard = Depends(dependencies.getScoreCardsCrud)) -> Any:
    scorecard = scoreCardCrud.get(scorecardID)
    return JSONResponse(status_code=status.HTTP_200_OK, content= jsonable_encoder({"object":scorecard}))

# Delete one ScoreCard with its own ID
@router.delete("/{scorecardID}")
def deleteScorecard(scorecardID:int , scoreCardCrud: crud.CRUDScoreCard = Depends(dependencies.getScoreCardsCrud)) -> Any:
    scorecard = scoreCardCrud.get(scorecardID)
    scoreCardCrud.delete(scorecardID)
    return JSONResponse("Deleted Successfully")

