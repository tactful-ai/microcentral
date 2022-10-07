from app.api.v1.endpoints import teams
from fastapi import APIRouter

apiRouter = APIRouter()

apiRouter.include_router(teams.router, prefix="/teams", tags=["teams"])
