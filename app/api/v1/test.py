from app.core.services import UsersService, get_users_service
from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("/testApi/")
def testGet(users_service: UsersService = Depends(get_users_service)):
    u = users_service.list()
    return {"message": "Hello", "Users: ": u}
