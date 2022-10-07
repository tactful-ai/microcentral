from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import setup_routes
from app.core.config import get_settings

#from fastapi.staticfiles import StaticFiles

#from .core.seeder import Seeder
#from .database import Base, engine, get_session
#from .views.dashboard import router as dashboard_router


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

    #Base.metadata.create_all(engine) # Create tables if they don't exist yet (idempotent) 

    #_app.mount("/app/static", StaticFiles(directory="app/static"), name="static")

    setup_routes(_app)
    #_app.include_router(dashboard_router, prefix="/dashboard")

    #print("Running Seeder")
    #Seeder(next(get_session())).seed()

    return _app

app = create_app()