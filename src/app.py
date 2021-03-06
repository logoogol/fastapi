import pathlib
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

BASE_DIR  = pathlib.Path(__file__).parent #src

app = FastAPI()
templates = Jinja2Templates(directory = BASE_DIR / "templates")

@app.get("/")
def home_view(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})
