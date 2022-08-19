from functools import lru_cache
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, BaseSettings, PostgresDsn, validator


class Settings(BaseSettings):
    PROJECT_NAME: str
    PROJECT_DESCRIPTION: Optional[str] = ""
    PROJECT_VERSION: Optional[str] = "1.0.0"

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    DB_DATABASE: str
    DATABASE_URI: Optional[PostgresDsn] = None

    SHOULD_SEED_THE_DB: Optional[bool] = False

    @validator("DATABASE_URI", pre=True)
    def assemble_db_connection(cls, value: Optional[PostgresDsn], values: Dict[str, Any]) -> Any:
        if isinstance(value, PostgresDsn):
            return value

        return f"postgresql://{values.get('DB_USER')}:{values.get('DB_PASSWORD')}@{values.get('DB_HOST')}:{values.get('DB_PORT')}/{values.get('DB_DATABASE')}"

    class Config:
        case_sensitive = True
        env_file = "../env"


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    return settings
