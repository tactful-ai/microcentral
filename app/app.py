from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.api.v1.test import router as test_api_router
from app.core.config import get_settings
from app.core.seeder import Seeder
from app.database import Base, engine, get_session
from app.views.dashboard import router as dashboard_router


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

    Base.metadata.create_all(engine)

    _app.mount("/app/static", StaticFiles(directory="app/static"), name="static")

    _app.include_router(test_api_router, prefix="/api/v1")
    _app.include_router(dashboard_router, prefix="/dashboard")

    if get_settings().SHOULD_SEED_THE_DB:
        print("Seeding the DB")
        Seeder(next(get_session())).seed()

    return _app
