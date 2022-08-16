from app.core.dependencies import get_db
from app.core.models.model import UserQueries
from app.core.services.test import TestService
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()



@router.get("/testApi/")
def testGet(db: Session = Depends(get_db)):
    u = UserQueries(db).get_all_users()
    return {"message":TestService().test(), 'Users: ': u}
