from app.core.services.authentication import JWTBearer
from fastapi import APIRouter, Depends

from ...core.services import TeamsService, get_service

router = APIRouter()


@router.get("/testApi/", dependencies=[Depends(JWTBearer())])
def testGet(teamsService: TeamsService = Depends(get_service("teams"))):
    return teamsService.list()
