from fastapi import APIRouter, Depends, status
from app.schemas import MicroserviceInDBBase, MicroserviceCreate, MicroserviceTeamScorecardBase, MicroserviceCreateApi, MicroserviceScoreCardCreate, MicroserviceUpdate, MicroserviceScoreCardUpdate
from app.crud import CRUDMicroservice, CRUDMicroserviceTeamScorecard, CRUDTeam, CRUDScoreCard, CRUDMicroserviceScoreCard
from typing import List
from app import dependencies
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from .exceptions import ExceptionCustom
import re


class Value(BaseModel):
    value: int | bool | float | str = Field(
        ..., title="Value", description="Value of the service")


router = APIRouter()


def format_code(name):
    code = re.sub(r'\s+', '-', name.strip())
    return code


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
            raise ExceptionCustom(status_code=404, detail="error_message")
    except Exception as x:
        error_message = "Service not found"
        raise ExceptionCustom(status_code=404, detail=error_message)
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
        raise ExceptionCustom(status_code=404, detail="Service not found")
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
        raise ExceptionCustom(status_code=400, detail="Code already exists")

    if not newmicroservice.name:
        raise ExceptionCustom(status_code=400, detail="Name cannot be empty")

    if len(newmicroservice.name) < 3:
        raise ExceptionCustom(
            status_code=400, detail="Name must be at least 3 characters long")

    if not newmicroservice.description:
        raise ExceptionCustom(
            status_code=400, detail="Description cannot be empty")

    if len(newmicroservice.description) > 500:
        raise ExceptionCustom(
            status_code=400, detail="Description cannot exceed 500 characters")

    teamobj = None
    scorecard_objs = []
    if newmicroservice.teamId:
        try:
            teamobj = teamservice.get(newmicroservice.teamId)
            if teamobj is None:
                raise ExceptionCustom(status_code=404, detail="Team not found")
        except Exception as x:
            error_message = 'Team Id was not found'
            raise ExceptionCustom(status_code=404, detail=error_message)
    else:
        pass

    if newmicroservice.scorecardids:
        scorecard_objs = scorecard.getByScoreCradIds(
            newmicroservice.scorecardids)
        if len(scorecard_objs) != len(newmicroservice.scorecardids):
            missing_ids = set(newmicroservice.scorecardids) - \
                {sc.id for sc in scorecard_objs}
            raise ExceptionCustom(
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
                raise ExceptionCustom(status_code=400, detail=error_message)
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
        raise ExceptionCustom(status_code=400, detail="Name cannot be empty")

    if len(updatemicroservice.name) < 3:
        raise ExceptionCustom(
            status_code=400, detail="Name must be at least 3 characters long")

    if not updatemicroservice.description:
        raise ExceptionCustom(
            status_code=400, detail="Description cannot be empty")

    if len(updatemicroservice.description) > 500:
        raise ExceptionCustom(
            status_code=400, detail="Description cannot exceed 500 characters")

    try:
        teamobj = teamservice.get(updatemicroservice.teamId)
        if teamobj is None:
            raise ExceptionCustom(status_code=404, detail="Not Found")
    except Exception as x:
        error_message = 'Team Id was not found'
        raise ExceptionCustom(status_code=404, detail=error_message)

    scorecard_objs = []
    if updatemicroservice.scorecardids:
        scorecard_objs = scorecard.getByScoreCradIds(
            updatemicroservice.scorecardids)
        if len(scorecard_objs) != len(updatemicroservice.scorecardids):
            missing_ids = set(updatemicroservice.scorecardids) - \
                {sc.id for sc in scorecard_objs}
            raise ExceptionCustom(
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
        raise ExceptionCustom(status_code=404, detail="Microservice not found")
    try:
        servicescorecard.deleteByServiceId(microservice_id)
    except Exception:
        error_message = "Can't delete Microservice ScoreCard"
        raise ExceptionCustom(
            status_code=404, detail="Can't delete Microservice ScoreCard")

    return {"message": "Microservice and associated scorecards successfully deleted"}
