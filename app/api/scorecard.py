from app import dependencies
from fastapi import APIRouter, Depends
from app import schemas, crud
from typing import Any, List
from app.utils.base import format_code, check_metric, stringify_value
from .exceptions import HTTPResponseCustomized
from .responses import ResponseCustomized
from app.schemas.apiResponse import CustomResponse
from app.schemas.scorecardServiceMetric import ScorecardServiceMetricCreate
from app.crud.scorecardServiceMetric import CRUDScoreCardServiceMetric


router = APIRouter()
@router.post("/", response_model=CustomResponse, response_class=ResponseCustomized)
def createScoreCard(scoreCardInput: ScorecardServiceMetricCreate,
                    scoreCardCrud: crud.CRUDScoreCard = Depends(
                        dependencies.getScoreCardsCrud),
                    serviceScorecardCrud: crud.CRUDMicroserviceScoreCard = Depends(
                        dependencies.getMicroserviceScoreCardsCrud),
                    scorecardMetricCrud: crud.CRUDScoreCardMetric = Depends(
                        dependencies.getScoreCardMetricsCrud),
                    serviceCrud: crud.CRUDMicroservice = Depends(
                        dependencies.getMicroservicesCrud),
                    metricCrud: crud.CRUDMetric = Depends(
                        dependencies.getMetricsCrud),
                    scorecard: crud.CRUDScoreCard = Depends(
                        dependencies.getScoreCardsCrud)
                    ):
    # Create the scorecard.
    scoreCardInput.code = format_code(scoreCardInput.name)
    scorecard = schemas.ScoreCardCreate(
        name=scoreCardInput.name,
        code=scoreCardInput.code,
        description=scoreCardInput.description
    )
    # if the scorecardids are passed duplicated
    servicesIDsSet = list(set(scoreCardInput.services))
    # i need to check if the serviceid is found or not
    services = serviceCrud.getByServiceIds(servicesIDsSet)
    serviceListToBeCreated = []
    if (len(services) != len(servicesIDsSet)):
        raise HTTPResponseCustomized(status_code=400, detail="Service not found")
    
    metricIds = []
    for metric in scoreCardInput.metrics:    
        metricIds.append(metric.id)
    metricIds = list(set(metricIds))
    metric_data = metricCrud.getByIds(metricIds)
    if (len(metric_data) != len(metricIds)):
        raise HTTPResponseCustomized(status_code=404, detail="Metric is not found")
    
    if (scoreCardCrud.getByScoreCardCode(scoreCardInput.code)):
        raise HTTPResponseCustomized(
            status_code=400, detail="Scorecard already found")
    try:
        obj = scoreCardCrud.create(scorecard)
        scorecardID = obj.id
    except Exception as e:
        raise HTTPResponseCustomized(status_code=422, detail=f"Error: {e}")

    metric_type_map = {metric.id:metric.type for metric in metric_data}
    for serviceid in servicesIDsSet:
        serviceScorecard = schemas.MicroserviceScoreCardCreate(
            scoreCardId=scorecardID,
            microserviceId=serviceid
        )
        serviceListToBeCreated.append(serviceScorecard)



    objects = []
    for metric in scoreCardInput.metrics:
        metricCreate = schemas.MetricTypeScorecard(
            id=metric.id,
            weight=metric.weight,
            desiredValue=metric.desiredValue,
            criteria=metric.criteria,
            type=metric_type_map[metric.id]  # Add the type directly from retrieved metric
        )
        objects.append(metricCreate)
    try:
        check_metric(objects)
    except Exception as e:
        scoreCardCrud.delete(scorecardID)
        raise e  # Return the error message
    for metric in scoreCardInput.metrics:
        metric.desiredValue = stringify_value(metric.desiredValue)
        scorecardmetric = schemas.ScoreCardMetricsCreate(
            scoreCardId=scorecardID,
            metricId=metric.id,
            criteria=metric.criteria,
            weight=metric.weight,
            desiredValue=metric.desiredValue
        )
        scorecardMetricCrud.create(scorecardmetric)

    for service in serviceListToBeCreated:
        serviceScorecardCrud.create(service)

    return ResponseCustomized("Scorecard created successfully")


@router.get("/", response_model=List[schemas.listScoreCard], response_class=ResponseCustomized)
def getAllScoreCard(scoreCardCrud: CRUDScoreCardServiceMetric = Depends(dependencies.getScorecardServiceMetric)):
    scorecard = scoreCardCrud.getlist()
    return ResponseCustomized(scorecard)


@router.get("/{scorecardID}", response_model=schemas.ScorecardServiceMetric, response_class=ResponseCustomized)
def getScoreCard(scorecardID: int, scoreCardCrud: CRUDScoreCardServiceMetric = Depends(dependencies.getScorecardServiceMetric)):
    scorecard = scoreCardCrud.getwithscorecardIDmetricandservice(scorecardID)
    return ResponseCustomized(scorecard)


# FINISHED
# Delete one ScoreCard with its own ID
@router.delete("/{scorecardID}", response_model=CustomResponse, response_class=ResponseCustomized)
def deleteScorecard(scorecardID: int,
                    scoreCardCrud: crud.CRUDScoreCard = Depends(
                        dependencies.getScoreCardsCrud),
                    scorecardService: crud.CRUDMicroserviceScoreCard = Depends(
                        dependencies.getMicroserviceScoreCardsCrud),
                    scorecardMetrics: crud.CRUDScoreCardMetric = Depends(dependencies.getScoreCardMetricsCrud)) -> Any:
    scoreCardCrud.delete(scorecardID)
    scorecardService.deleteByScorecardId(scorecardID)
    scorecardMetrics.deleteByScorecardId(scorecardID)
    return ResponseCustomized("Scorecard deleted successfully")
