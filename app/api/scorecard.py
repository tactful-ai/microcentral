from app import dependencies
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from app import schemas, crud
from typing import Any, List
from app.utils.base import format_code, check_metric, stringify_value
from .exceptions import HTTPResponseCustomized, ResponseCustomized
from app.schemas.scoreCardMetrics import CustomJSONEncoder
from fastapi.responses import ORJSONResponse
from app.schemas.apiResponse import CustomResponse

router = APIRouter()
# VALIDATIONS DONE
# 1) scorecard is already found or not using its code
# 2) if the list of serviceIDs contains duplicated IDs it will be cleared as it is gonna be set not list
# 3) if the scorecard is found or that id is just dummy id
# 4) made the func check_unique_id to check if the metrics passed is the same object passed twice or not
# 5) check_metric_weight to see the sum of the weights of the metrics
# 6) check if the metric is found or not
# 7) check the criteria if it is in the enum
@router.post("/", response_model=None)
def createScoreCard(scoreCardInput: schemas.scorecardServiceMetricCreate,
                    scoreCardCrud: crud.CRUDScoreCard = Depends(dependencies.getScoreCardsCrud),
                    serviceScorecardCrud: crud.CRUDMicroserviceScoreCard = Depends(dependencies.getMicroserviceScoreCardsCrud),
                    scorecardMetricCrud: crud.CRUDScoreCardMetric = Depends(dependencies.getScoreCardMetricsCrud),
                    serviceCrud: crud.CRUDMicroservice = Depends(dependencies.getMicroservicesCrud),
                    metricCrud: crud.CRUDMetric = Depends(dependencies.getMetricsCrud),
                    scorecard: crud.CRUDScoreCard = Depends(dependencies.getScoreCardsCrud)
                    ):
    # Create the scorecard.
    scoreCardInput.code = format_code(scoreCardInput.name)
    scorecard = schemas.ScoreCardCreate(
        name=scoreCardInput.name,
        code=scoreCardInput.code,
        description=scoreCardInput.description
    )
    if (scoreCardCrud.getByScoreCardCode(scoreCardInput.code)):
        raise HTTPResponseCustomized(status_code=400, detail="Scorecard already found")
    # DELETE 
    else:
        if (scoreCardCrud.getlatestID() == None):
            scorecardID = 1
        else:
            scorecardID = scoreCardCrud.getlatestID() + 1
        

    # if the scorecardids are passed duplicated
    servicesIDsSet = set(scoreCardInput.services)
    # i need to check if the serviceid is found or not 
    serviceList = serviceCrud.getByServiceId(servicesIDsSet)
    print(serviceList)
    serviceListToBeCreated = []
    for service in serviceList:
        if(service):
            serviceScorecard = schemas.MicroserviceScoreCardCreate(
            scoreCardId=scorecardID,
            microserviceId=service
            )
            serviceListToBeCreated.append(serviceScorecard)
        else:
            raise HTTPResponseCustomized(status_code=404, detail="Service not found")
    

    objects = []
    for metric in scoreCardInput.metrics:
            metric_data = metricCrud.getById(metric.id)  # Get the metric data
            if (metric_data == None):
                raise HTTPResponseCustomized(status_code=404, detail="Metric is not found")
            metricCreate = schemas.metricTypeScorecard(
                id=metric.id,
                weight=metric.weight,
                desiredValue=metric.desiredValue,
                criteria=metric.criteria,
                type=metric_data.type  # Add the type directly from retrieved metric
            )
            objects.append(metricCreate)

    check_metric(objects)
    for metric in scoreCardInput.metrics:
        if (metricCrud.getById(metric.id)):
            metric.desiredValue = stringify_value(metric.desiredValue)
            scorecardmetric = schemas.ScoreCardMetricsCreate(
                scoreCardId= scorecardID,
                metricId= metric.id,
                criteria= metric.criteria,
                weight= metric.weight,                                
                desiredValue= metric.desiredValue
            )
        else:
            raise HTTPResponseCustomized(status_code=404, detail="Metric not found")
        try: 
            scorecardMetricCrud.create(scorecardmetric)
        except Exception as e:
            raise HTTPResponseCustomized(status_code=422,detail= f"Error: {e}")
    
    for service in serviceListToBeCreated:
        try:
            serviceScorecardCrud.create(service)
        except Exception as e:
            scorecardMetricCrud.deleteByScorecardId(scorecardID)
            raise HTTPResponseCustomized(status_code=422,detail= f"Error: {e}")
        
    try:
        scoreCardCrud.create(scorecard)
    except Exception as e:
            scorecardMetricCrud.deleteByScorecardId(scorecardID)
            serviceScorecardCrud.deleteByScorecardId(scorecardID)
            raise HTTPResponseCustomized(status_code=422,detail= f"Error: {e}")
    raise HTTPResponseCustomized(status_code=201, detail="Scorecard created successfully")

@router.get("/", response_model=List[schemas.listScoreCard], response_class=ResponseCustomized)
def getAllScoreCard(scoreCardCrud: crud.CRUDScoreCardServiceMetric = Depends(dependencies.getScorecardServiceMetric)):
    scorecard = scoreCardCrud.getlist()
    #print(scorecard)
    scorecard = jsonable_encoder(scorecard)
    #print(scorecard)
    return scorecard
"""
@router.get("/{scorecardID}", response_model=schemas.ScoreCard)
def getScoreCard(scorecardID: int, scoreCardCrud: crud.CRUDScoreCardServiceMetric = Depends(dependencies.getScorecardServiceMetric)):
    scorecard = scoreCardCrud.getwithscorecardIDmetricandservice(scorecardID)
    #print(scorecard)
    scorecard = jsonable_encoder(scorecard)
    #print(scorecard)
    return ResponseCustomized(status_code=200, content=scorecard)
"""
# Delete one ScoreCard with its own ID
@router.delete("/{scorecardID}",response_model=CustomResponse ,response_class=ResponseCustomized)
def deleteScorecard(scorecardID: int,
                    scoreCardCrud: crud.CRUDScoreCard = Depends(dependencies.getScoreCardsCrud),
                    scorecardService: crud.CRUDMicroserviceScoreCard = Depends(dependencies.getMicroserviceScoreCardsCrud),
                    scorecardMetrics: crud.CRUDScoreCardMetric = Depends(dependencies.getScoreCardMetricsCrud)) -> Any:
    
    scoreCardCrud.delete(scorecardID)
    scorecardService.deleteByScorecardId(scorecardID)
    scorecardMetrics.deleteByScorecardId(scorecardID)
    return "Scorecard deleted successfully"
