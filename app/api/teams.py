from typing import Any, List
from app import crud, schemas
from app import dependencies
from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("/", response_model=List[schemas.Team])
def read_teams(teamsCrud: crud.CRUDTeam = Depends(dependencies.getTeamsCrud), skip: int = 0, limit: int = 100) -> Any:
    """
    Retrieve teams.
    """
    teams = teamsCrud.list(skip=skip, limit=limit)
    return teams


@router.post("/", response_model=schemas.Team)
def create_team(team: schemas.TeamCreate, teamsCrud: crud.CRUDTeam = Depends(dependencies.getTeamsCrud)) -> Any:
    """
    Create new team.
    """
    return teamsCrud.create(team)
