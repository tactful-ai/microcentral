from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/testView/", response_class=HTMLResponse)
def create_user(request: Request):
    return templates.TemplateResponse("test.html", {"request": request, "message": "Hello World from test View"})
