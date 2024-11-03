from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get("/")
def read_root():
    return {'message': 'Добро пожаловать в КотоВыбор'}

@app.get("/cats")
def read_cats():
    return [{"id": 1, "name": "Whiskers"}, {"id": 2, "name": "Mittens"}]


# if __name__ == "__main__":
#     uvicorn.run(app)