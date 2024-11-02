from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_root():
    return {'message': 'Добро пожаловать в КотоВыбор'}

@app.get("/cats")
def read_cats():
    return [{"id": 1, "name": "Whiskers"}, {"id": 2, "name": "Mittens"}]
