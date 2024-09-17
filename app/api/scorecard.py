from app import dependencies
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from app import schemas, crud
from typing import Any, List
from app.utils.base import format_code, check_metric, stringify_value
from .exceptions import HTTPResponseCustomized
from .responses import ResponseCustomized
from fastapi.responses import ORJSONResponse
from app.schemas.apiResponse import CustomResponse
from app.schemas.scorecardServiceMetric import ScorecardServiceMetricCreate
from app.crud.scorecardServiceMetric import CRUDScoreCardServiceMetric


router = APIRouter()
# VALIDATIONS DONE
# 1) scorecard is already found or not using its code
# 2) if the list of serviceIDs contains duplicated IDs it will be cleared as it is gonna be set not list
# 3) if the scorecard is found or that id is just dummy id
# 4) made the func check_unique_id to check if the metrics passed is the same object passed twice or not
# 5) check_metric_weight to see the sum of the weights of the metrics
# 6) check if the metric is found or not
# 7) check the criteria if it is in the enum
# FINISHED


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
    if (scoreCardCrud.getByScoreCardCode(scoreCardInput.code)):
        raise HTTPResponseCustomized(
            status_code=400, detail="Scorecard already found")
    try:
        obj = scoreCardCrud.create(scorecard)
        scorecardID = obj.id
    except Exception as e:
        raise HTTPResponseCustomized(status_code=422, detail=f"Error: {e}")

    # if the scorecardids are passed duplicated
    servicesIDsSet = list(set(scoreCardInput.services))
    # i need to check if the serviceid is found or not
    serviceListToBeCreated = []
    for serviceid in servicesIDsSet:
        service = serviceCrud.getByServiceId(serviceid)
        if (service):
            serviceScorecard = schemas.MicroserviceScoreCardCreate(
                scoreCardId=scorecardID,
                microserviceId=serviceid
            )
            serviceListToBeCreated.append(serviceScorecard)
        else:
            scoreCardCrud.delete(scorecardID)
            raise HTTPResponseCustomized(
                status_code=400, detail="Service not found")

    objects = []
    for metric in scoreCardInput.metrics:
        metric_data = metricCrud.getById(metric.id)  # Get the metric data
        if (metric_data == None):
            scoreCardCrud.delete(scorecardID)
            raise HTTPResponseCustomized(
                status_code=404, detail="Metric is not found")
        metricCreate = schemas.MetricTypeScorecard(
            id=metric.id,
            weight=metric.weight,
            desiredValue=metric.desiredValue,
            criteria=metric.criteria,
            type=metric_data.type  # Add the type directly from retrieved metric
        )
        objects.append(metricCreate)
    try:
        if (objects):
            check_metric(objects)
    except Exception as e:
        scoreCardCrud.delete(scorecardID)
        check_metric(objects)  # Return the error message
    for metric in scoreCardInput.metrics:
        if (metricCrud.getById(metric.id)):
            metric.desiredValue = stringify_value(metric.desiredValue)
            scorecardmetric = schemas.ScoreCardMetricsCreate(
                scoreCardId=scorecardID,
                metricId=metric.id,
                criteria=metric.criteria,
                weight=metric.weight,
                desiredValue=metric.desiredValue
            )
        else:
            scoreCardCrud.delete(scorecardID)
            raise HTTPResponseCustomized(
                status_code=404, detail="Metric not found")
        try:
            scorecardMetricCrud.create(scorecardmetric)
        except Exception as e:
            scoreCardCrud.delete(scorecardID)
            raise HTTPResponseCustomized(status_code=422, detail=f"Error: {e}")

    for service in serviceListToBeCreated:
        try:
            serviceScorecardCrud.create(service)
        except Exception as e:
            scorecardMetricCrud.deleteByScorecardId(scorecardID)
            scoreCardCrud.delete(scorecardID)
            raise HTTPResponseCustomized(status_code=422, detail=f"Error: {e}")

    return ResponseCustomized("Scorecard created successfully")


@router.get("/", response_model=List[schemas.listScoreCard], response_class=ResponseCustomized)
def getAllScoreCard(scoreCardCrud: CRUDScoreCardServiceMetric = Depends(dependencies.getScorecardServiceMetric)):
    scorecard = scoreCardCrud.getlist()
    return ResponseCustomized(scorecard)


@router.get("/{scorecardID}", response_model=schemas.ScoreCard)
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
