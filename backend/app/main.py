from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.api import apiRouter
from app.core.config import get_settings


def create_app() -> FastAPI:
    _app = FastAPI(title=get_settings().PROJECT_NAME, description=get_settings().PROJECT_DESCRIPTION, version=get_settings().PROJECT_VERSION)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in get_settings().BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Just for checking if the app is up and running
    @_app.get("/health")
    async def health() -> str:
        return "ok"

    _app.include_router(apiRouter, prefix=get_settings().API_V1_STR)

    return _app

app = create_app()
