import os, sys
sys.dont_write_bytecode = True
sys.path.append(os.getcwd())
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from routers.cat_router import cat_router
from pathlib import Path
from database import Base, engine
from models.cat import Cat

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(cat_router)


# Constructing the absolute path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
static_dir = os.path.join(BASE_DIR, "static")

# Mounting the static directory
app.mount("/static", StaticFiles(directory=static_dir), name="static")

templates_dir = os.path.join(os.path.dirname(__file__), "templates")
templates = Jinja2Templates(directory=templates_dir)

app.include_router(cat_router, prefix="/cats")

@app.get("/")
async def read_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# @app.get("/cats")
# def read_cats():
#     return [{"id": 1, "name": "Whiskers"}, {"id": 2, "name": "Mittens"}]
