import os, sys
sys.dont_write_bytecode = True
sys.path.append(os.getcwd())
from sqlalchemy import Column, Integer, String
from database import Base 

class Cat(Base):
    __tablename__ = "cats"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    breed = Column(Integer)
    description = Column(Integer)
    
    def __init__(self, name: str, age: int, breed: str, description: str):  # Ensure description is included
        self.name = name
        self.age = age
        self.breed = breed
        self.description = description

    def __repr__(self):
        return f"<Cat(name={self.name}, age={self.age}, breed = {self.breed}, description = {self.description})>"