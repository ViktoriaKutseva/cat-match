import os, sys
sys.dont_write_bytecode = True
sys.path.append(os.getcwd())
from fastapi import FastAPI
import uvicorn
from routers.cat_router import cat_router



app = FastAPI()

app.include_router(cat_router, prefix="/cats")

@app.get("/")
def read_root():
    return {'message': 'Добро пожаловать в КотоВыбор'}

@app.get("/cats")
def read_cats():
    return [{"id": 1, "name": "Whiskers"}, {"id": 2, "name": "Mittens"}]
