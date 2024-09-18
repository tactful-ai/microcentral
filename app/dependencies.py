from typing import Generator

from app import crud
from .database.session import SessionLocal
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

def getMicroservicesCrud(db_session: Session = Depends(get_db)):
    return crud.CRUDMicroservice(db_session)

def getMetricsCrud(db_session: Session = Depends(get_db)):  
    return crud.CRUDMetric(db_session)

def getScoreCardsCrud(db_session: Session = Depends(get_db)):
    return crud.CRUDScoreCard(db_session)

def getScoreCardMetricsCrud(db_session: Session = Depends(get_db)):
    return crud.CRUDScoreCardMetric(db_session) 

def getMicroserviceScoreCardsCrud(db_session: Session = Depends(get_db)):   
    return crud.CRUDMicroserviceScoreCard(db_session)   

def getServiceMetricsCrud(db_session: Session = Depends(get_db)):   
    return crud.CRUDServiceMetric(db_session)

def getMicroserviceTeamScoreCardCrud(db_session: Session = Depends(get_db)):
    return crud.CRUDMicroserviceTeamScorecard(db_session)

def getMicroserviceInfoCrud(db_session: Session = Depends(get_db)):
    return crud.CRUDMicroserviceInfo(db_session)

def getMetricInfoCrud(db_session: Session = Depends(get_db)):
    return crud.CRUDMetricInfo(db_session)
