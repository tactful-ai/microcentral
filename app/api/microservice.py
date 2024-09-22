from fastapi import APIRouter, Depends, status
from app.schemas import MicroserviceInDBBase, MicroserviceCreate, MicroserviceTeamScorecardBase, MicroserviceCreateApi, MicroserviceScoreCardCreate, MicroserviceUpdate, ServiceMetricReading, ServiceMetricCreate
from app.crud import CRUDMicroservice, CRUDMicroserviceTeamScorecard, CRUDTeam, CRUDScoreCard, CRUDMicroserviceScoreCard, CRUDMetric, CRUDServiceMetric
from typing import List, Optional
from datetime import datetime, timezone
from app import dependencies
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from .exceptions import HTTPResponseCustomized
from app.utils.base import format_code
from app.utils import utity_datatype


class Value(BaseModel):
    value: int | bool | float | str = Field(
        ..., title="Value", description="Value of the service")


router = APIRouter()


@router.get("/", response_model=List[MicroserviceInDBBase])
def get_all_services(microServices: CRUDMicroservice = Depends(dependencies.getMicroservicesCrud)):
    return microServices.getAllServicesWithTeamName()


@router.get("/{service_id}", response_model=MicroserviceInDBBase)
async def get_one_service(service_id: int, microServices: CRUDMicroservice = Depends(dependencies.getMicroservicesCrud), teamService: CRUDTeam = Depends(dependencies.getTeamsCrud)):
    teamobj = None
    service = None

    try:
        service = microServices.get(service_id)
        if service is None:
            raise HTTPResponseCustomized(
                status_code=404, detail="error_message")
    except Exception as x:
        error_message = "Service not found"
        raise HTTPResponseCustomized(status_code=404, detail=error_message)
    if service.teamId:
        try:
            teamobj = teamService.get(service.teamId)
        except Exception as x:
            pass
    return MicroserviceInDBBase(
        id=service.id,
        name=service.name,
        description=service.description,
        code=service.code,
        team_name=teamobj.name if teamobj else None,
    )


@router.get("/{service_id}/details", response_model=MicroserviceTeamScorecardBase)
async def getmicroservice_with_teamAndScorecards(service_id: int, microServicesteamScorecard: CRUDMicroserviceTeamScorecard = Depends(dependencies.getMicroserviceTeamScoreCardCrud)):
    service = microServicesteamScorecard.getByServiceIdWithTeamAndScoreDetails(
        service_id)
    if service is None:
        raise HTTPResponseCustomized(
            status_code=404, detail="Service not found")
    return service


@router.post("/", response_model=None)
def create_microservice(newmicroservice: MicroserviceCreateApi,
                        microservice: CRUDMicroservice = Depends(
                            dependencies.getMicroservicesCrud),
                        teamservice: CRUDTeam = Depends(
                            dependencies.getTeamsCrud),
                        servicescorecard: CRUDMicroserviceScoreCard = Depends(
                            dependencies.getMicroserviceScoreCardsCrud),
                        scorecard: CRUDScoreCard = Depends(dependencies.getScoreCardsCrud)):

    microservice.check_service_name_exists(newmicroservice.name)
    formatted_code = format_code(newmicroservice.name)
    existing_microservice = microservice.get_by_code(formatted_code)
    if existing_microservice:
        raise HTTPResponseCustomized(
            status_code=400, detail="Code already exists")

    if not newmicroservice.name:
        raise HTTPResponseCustomized(
            status_code=400, detail="Name cannot be empty")

    if len(newmicroservice.name) < 3:
        raise HTTPResponseCustomized(
            status_code=400, detail="Name must be at least 3 characters long")

    if not newmicroservice.description:
        raise HTTPResponseCustomized(
            status_code=400, detail="Description cannot be empty")

    if len(newmicroservice.description) > 500:
        raise HTTPResponseCustomized(
            status_code=400, detail="Description cannot exceed 500 characters")

    teamobj = None
    scorecard_objs = []
    if newmicroservice.teamId:
        try:
            teamobj = teamservice.get(newmicroservice.teamId)
            if teamobj is None:
                raise HTTPResponseCustomized(
                    status_code=404, detail="Team not found")
        except Exception as x:
            error_message = 'Team Id was not found'
            raise HTTPResponseCustomized(
                status_code=404, detail=error_message)
    else:
        pass

    if newmicroservice.scorecardids:
        scorecard_objs = scorecard.getByScoreCradIds(
            newmicroservice.scorecardids)
        if len(scorecard_objs) != len(newmicroservice.scorecardids):
            missing_ids = set(newmicroservice.scorecardids) - \
                {sc.id for sc in scorecard_objs}
            raise HTTPResponseCustomized(
                status_code=404, detail=f"ScoreCard(s) with ID(s): {missing_ids} were not found")

    created_microservice = microservice.create(MicroserviceCreate(name=newmicroservice.name,
                                                                  description=newmicroservice.description,
                                                                  teamId=newmicroservice.teamId,
                                                                  code=formatted_code))
    if newmicroservice.scorecardids is not None:
        for scorecard_obj in scorecard_objs:
            try:
                servicescorecard.create(MicroserviceScoreCardCreate(
                    microserviceId=created_microservice.id,
                    scoreCardId=scorecard_obj.id
                ))
            except Exception as x:
                error_message = f"Failed to create relationship for ScoreCard ID: {scorecard_obj.id}. Reason: {str(x)}"
                raise HTTPResponseCustomized(
                    status_code=400, detail=error_message)
    return created_microservice

    # update operation


@router.put("/{servise_id}", response_model=None)
def update_microservice(microservice_id: int, updatemicroservice: MicroserviceCreateApi,
                        microservice: CRUDMicroservice = Depends(
                            dependencies.getMicroservicesCrud),
                        teamservice: CRUDTeam = Depends(
                            dependencies.getTeamsCrud),
                        servicescorecard: CRUDMicroserviceScoreCard = Depends(
                            dependencies.getMicroserviceScoreCardsCrud),
                        scorecard: CRUDScoreCard = Depends(dependencies.getScoreCardsCrud)):

    if not updatemicroservice.name:
        raise HTTPResponseCustomized(
            status_code=400, detail="Name cannot be empty")

    if len(updatemicroservice.name) < 3:
        raise HTTPResponseCustomized(
            status_code=400, detail="Name must be at least 3 characters long")

    if not updatemicroservice.description:
        raise HTTPResponseCustomized(
            status_code=400, detail="Description cannot be empty")

    if len(updatemicroservice.description) > 500:
        raise HTTPResponseCustomized(
            status_code=400, detail="Description cannot exceed 500 characters")

    try:
        teamobj = teamservice.get(updatemicroservice.teamId)
        if teamobj is None:
            raise HTTPResponseCustomized(
                status_code=404, detail="Not Found")
    except Exception as x:
        error_message = 'Team Id was not found'
        raise HTTPResponseCustomized(status_code=404, detail=error_message)

    scorecard_objs = []
    if updatemicroservice.scorecardids:
        scorecard_objs = scorecard.getByScoreCradIds(
            updatemicroservice.scorecardids)
        if len(scorecard_objs) != len(updatemicroservice.scorecardids):
            missing_ids = set(updatemicroservice.scorecardids) - \
                {sc.id for sc in scorecard_objs}
            raise HTTPResponseCustomized(
                status_code=404, detail=f"ScoreCard(s) with ID(s): {missing_ids} were not found")

    formatted_code = format_code(updatemicroservice.name)
    updated_microservice = microservice.update(microservice_id, MicroserviceUpdate(
        name=updatemicroservice.name,
        description=updatemicroservice.description,
        teamId=updatemicroservice.teamId,
        code=formatted_code
    ))
    servicescorecard.deleteByServiceId(microservice_id)
    for scorcardid in updatemicroservice.scorecardids:
        servicescorecard.create(MicroserviceScoreCardCreate(
            microserviceId=microservice_id, scoreCardId=scorcardid))

    return updated_microservice


@router.delete("/{service_id}")
def delete_microservice(
        microservice_id: int,
        microservice: CRUDMicroservice = Depends(
            dependencies.getMicroservicesCrud),
        servicescorecard: CRUDMicroserviceScoreCard = Depends(dependencies.getMicroserviceScoreCardsCrud)):

    try:
        microservice.delete(microservice_id)
    except Exception:
        error_message = "Can't delete Microservice"
        raise HTTPResponseCustomized(
            status_code=404, detail="Microservice not found")
    try:
        servicescorecard.deleteByServiceId(microservice_id)
    except Exception:
        error_message = "Can't delete Microservice ScoreCard"
        raise HTTPResponseCustomized(
            status_code=404, detail="Can't delete Microservice ScoreCard")

    return {"message": "Microservice and associated scorecards successfully deleted"}


@router.get("/{                                                                                                                                                         }/metric_reading", response_model=list[ServiceMetricReading])
def get_metrics(service_id: int, from_date: Optional[datetime] = None,
                to_date: Optional[datetime] = None,  service_metric_crud: CRUDServiceMetric = Depends(dependencies.getServiceMetricsCrud)):

    metrics = service_metric_crud.get_metric_values_by_service(
        service_id, from_date, to_date)

    if not metrics:
        raise HTTPResponseCustomized(
            status_code=404, detail="Metrics not found for this service and metric.")

    return metrics


@router.post("/{service_id}/{metric_id}/reading", response_model=None)
def create_metric_reading(
    service_id: int,
    metric_id: int,
    newmservicemetric: ServiceMetricCreate,
    microservice: CRUDMicroservice = Depends(
        dependencies.getMicroservicesCrud),
    servicemetric: CRUDServiceMetric = Depends(
        dependencies.getServiceMetricsCrud),
    metric: CRUDMetric = Depends(dependencies.getMetricsCrud),
):

    microservice_obj = microservice.get(service_id)
    if not microservice_obj:
        raise HTTPResponseCustomized(
            status_code=404, detail="Service not found")

    metric_obj = metric.get(metric_id)
    if not metric_obj:
        raise HTTPResponseCustomized(
            status_code=404, detail="Metric not found")

    if newmservicemetric.serviceId != service_id:
        raise HTTPResponseCustomized(
            status_code=400, detail="Microservice ID does not match")

    if newmservicemetric.metricId != metric_id:
        raise HTTPResponseCustomized(
            status_code=400, detail="Metric ID does not match")

    metric_value = utity_datatype.parse_stringified_value(
        newmservicemetric.value, metric_obj.type)

    date = newmservicemetric.timestamp or datetime.now()
    date_aware = date.replace(tzinfo=timezone.utc)
    if date_aware > datetime.now(timezone.utc):
        raise HTTPResponseCustomized(
            status_code=400, detail="Timestamp cannot be in the future")

    service_metric = servicemetric.create(
        ServiceMetricCreate(
            serviceId=service_id,
            metricId=metric_id,
            value=metric_value,
            timestamp=date,
        )
    )

    return service_metric
