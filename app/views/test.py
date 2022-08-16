
from app.core.dependencies import get_db
from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")

@router.get("/testView/", response_class=HTMLResponse)
def create_user(request: Request, db: Session = Depends(get_db)):
    print("Url: ", request.url)
    print("templates: ", templates)
    return templates.TemplateResponse("test.html", {"request": request ,"message": "Hello World from test View"}) 
