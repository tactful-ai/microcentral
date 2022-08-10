from app.core.dependencies import get_db
from app.core.services.test import TestService
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()



@router.get("/testApi/")
def create_user(db: Session = Depends(get_db)):
    return {"message":TestService().test()}
