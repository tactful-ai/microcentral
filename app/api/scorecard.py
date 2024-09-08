from app import dependencies 
from fastapi.exceptions import RequestValidationError
from app.schemas import ServiceMetricCreate, MetricCreate, scoreCard, microserviceScoreCard, scorecardServiceMetric
from fastapi import APIRouter, Depends, Request, exception_handlers, status, Response, HTTPException
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field
from app.crud import CRUDMetric, CRUDServiceMetric, CRUDMicroserviceScoreCard, CRUDMicroservice, CRUDScoreCardServiceMetric
from app import schemas, models, crud
from typing import Any, List
import json
from fastapi.routing import APIRoute
from app.utils.base import format_code
from .exceptions import HTTPResponseCustomized


router = APIRouter()

@router.post("/", response_model=schemas.ScoreCard)
def createScoreCard(scoreCard: schemas.scorecardServiceMetric, scoreCardCrud: crud.CRUDScoreCardServiceMetric = Depends(dependencies.getScorecardServiceMetric)) -> Any:
    try:
        scoreCard.services = jsonable_encoder(scoreCard.services)
        scoreCard.services = json.dumps(scoreCard.services)
        scoreCard.metrics = jsonable_encoder(scoreCard.metrics)
        scoreCard.metrics = json.dumps(scoreCard.metrics)
        scoreCard.code = format_code(scoreCard.name)
        return scoreCard
    except:
        return scoreCard


# I get all the scorecards id then go to microserviceSCORECARD to get all ids of microservices related to one scorecardID
@router.get("/", response_model=List[schemas.GetScoreCard])
def getAllScoreCard(scoreCardCrud: crud.CRUDScoreCard = Depends(dependencies.getScoreCardsCrud), serviceCrud: crud.CRUDMicroserviceScoreCard= Depends(dependencies.getMicroserviceScoreCardsCrud)):
    scoreCards = scoreCardCrud.list()
    servicesID = []
    microservices = []
    for scorecard in scoreCards:
        serviceid = serviceCrud.getservice(scorecard.id)
        servicesID.append(serviceid)
    for serviceID in servicesID:
        microservice = serviceCrud.getByServiceId(serviceID)
        microservice = jsonable_encoder(microservice)
        microservices.append(microservice)
    return "Hello World"


@router.get("/{scorecardID}", response_model=schemas.ScoreCard)
def getScoreCard(scorecardID: int, scoreCardCrud: crud.CRUDScoreCardServiceMetric = Depends(dependencies.getScorecardServiceMetric)) -> Any:
    scorecard = scoreCardCrud.getwithscorecardIDmetricandservice(scorecardID)
    scorecard = jsonable_encoder(scorecard)
    return HTTPResponseCustomized(status_code=200, detail=scoreCard)

# Delete one ScoreCard with its own ID
@router.delete("/{scorecardID}")
def deleteScorecard(scorecardID:int , scoreCardCrud: crud.CRUDScoreCard = Depends(dependencies.getScoreCardsCrud)) -> Any:
    scoreCardCrud.delete(scorecardID)
    raise HTTPResponseCustomized(status_code = 200, detail = "Scorecard Has Been Deleted Successfully")

