from typing import Generator

from app import crud
from app.database.session import SessionLocal
from fastapi import Depends
from sqlalchemy.orm import Session


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

################# CRUDs #################
def getTeamsCrud(db_session: Session = Depends(get_db)):
    return crud.CRUDTeam(db_session)
