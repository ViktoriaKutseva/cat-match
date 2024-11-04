from sqlalchemy.orm import Session  # Импортируем объект Session из SQLAlchemy
from models.cat import Cat  # Импортируем модель Cat из папки models

def create_cat(db: Session, name: str, age: int, breed: str):
    new_cat = Cat(name=name, age=age, breed=breed)
    db.add(new_cat)
    db.commit()
    db.refresh(new_cat)
    return new_cat

def get_cats(db: Session):
    return db.query(Cat).all()

def get_cat(db: Session, cat_id: int):
    return db.query(Cat).filter(Cat.id == cat_id).first()

def update_cat(db: Session, cat_id: int, name: str = None, age: int = None, breed: str = None):
    cat = db.query(Cat).filter(Cat.id == cat_id).first()
    if cat:  
        if name:
            cat.name = name  
        if age:
            cat.age = age
        if breed:
            cat.breed = breed
        db.commit()
        db.refresh
    return cat

def delete_cat(db:Session, cat_id: int):
    cat = db.query(Cat).filter(Cat.id == cat_id).first()
    if cat:
        db.delete(cat)
        db.commit()
    return cat 
