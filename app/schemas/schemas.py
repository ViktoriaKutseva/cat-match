from pydantic import BaseModel

class CatUpdate(BaseModel):
    name: str
    age: int
    breed: str
    description: str

    # Это нужно для корректной работы с SQLAlchemy и сериализации/десериализации
    class Config:
        orm_mode = True