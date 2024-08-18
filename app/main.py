from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.api.api import apiRouter
from app.core.config import settings
from app.views.dashboard import router as dashboard_router


def create_app() -> FastAPI:
    _app = FastAPI(title=settings.PROJECT_NAME, description=settings.PROJECT_DESCRIPTION, version=settings.PROJECT_VERSION)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    ## for try
    @_app.get("/")
    async def root():
          return {"message": "Hello World"}

    # Just for checking if the app is up and running
    @_app.get("/health")
    async def health() -> str:
        return "ok"

    _app.mount("/app/static", StaticFiles(directory="app/static"), name="static")

    # setup_routes(_app)
    _app.include_router(dashboard_router, prefix="/dashboard")
    _app.include_router(apiRouter, prefix=settings.API_V1_STR)

    return _app

app = create_app()