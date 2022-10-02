from functools import lru_cache
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import scoped_session, sessionmaker

from .core.config import get_settings

engine = create_engine(get_settings().DATABASE_URI, pool_pre_ping=True)


@lru_cache
def create_session() -> scoped_session:
    Session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
    return Session

# Dependency
def get_session() -> Generator[scoped_session, None, None]:
    Session = create_session()
    try:
        yield Session
    finally:
        Session.remove()

@as_declarative()
class Base:
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + 's'
