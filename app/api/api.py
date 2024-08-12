from . import teams, metrics ,microService
from fastapi import APIRouter

apiRouter = APIRouter()

apiRouter.include_router(teams.router, prefix="/teams", tags=["teams"])

apiRouter.include_router(metrics.router, prefix="/metrics", tags=["metrics"])

apiRouter.include_router(microService.router, prefix="/services", tags=["microService"])