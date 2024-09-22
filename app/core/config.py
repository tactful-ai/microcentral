from functools import lru_cache
from typing import Any, Dict, List, Optional, Union

from pydantic_settings import BaseSettings, SettingsConfigDict 
from pydantic import AnyHttpUrl, PostgresDsn, field_validator


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore')
    
    PROJECT_NAME: str
    PROJECT_DESCRIPTION: Optional[str] = ""
    PROJECT_VERSION: Optional[str] = "1.0.0"

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ['http://localhost:3000']

    @field_validator("BACKEND_CORS_ORIGINS")
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    API_V1_STR: str = "/api/v1"

    SHOULD_SEED_THE_DB: Optional[bool] = False
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 30 # 30 days

    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"

    DATABASE_URI: PostgresDsn




settings = Settings()
