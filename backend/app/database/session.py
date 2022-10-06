from app.core.config import get_settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(get_settings().DATABASE_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
