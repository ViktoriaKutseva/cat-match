import os, sys
sys.dont_write_bytecode = True
sys.path.append(os.getcwd())
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies import get_db
from services.crud import create_cat, get_cat, get_cats, update_cat, delete_cat


cat_router = APIRouter()

@cat_router.post("/cats/")
async def add_cat_endpoint(name: str, age: int, breed: str, description: str, db: Session = Depends(get_db)):
    new_cat = create_cat(db, name, age, breed, description)
    if new_cat:
        return {"message": "Кисонька в базе", "и это": new_cat}
    else:
        return {"Что-то не то с кисонькой"}

@cat_router.get("/cats")
async def read_cats_endpoint(db: Session = Depends(get_db)):
    all_cats = get_cats(db)
    print(all_cats)
    if all_cats:
        return {"Так вот же они, на пригорочке": all_cats}
    else:
        return {"Гиде кисоньки???"}

@cat_router.get("/cats/{cat_id}")
async def read_cat_endpoint(cat_id: int, db: Session = Depends(get_db)):
    specific_cat = get_cat(db, cat_id) 
    if specific_cat:
        return {"Вот ваш пирожочек", specific_cat}
    else:
        return {"Пирожок не найден("}

@cat_router.delete("/cats/{cat_id}")
async def delete_cats_endpoint(cat_id: int, db: Session = Depends(get_db)):
    deleted_cat = delete_cat(db, cat_id)
    if deleted_cat:
        return {"message": "Пиздюк пристроен", "cat": deleted_cat}
    else:
        return {"С пиздюком что-то пошло не так"}
    
@cat_router.put("/cats/{cat_id}")
async def update_cat_endpoin(name: str, age: int, breed: str, description: str, db: Session = Depends(get_db)):
    updated_cat = update_cat(db, name, age, breed, description)
    if updated_cat:
        return{"message": "Обновленная машина", "cat": updated_cat}
    else:
        return{"Чет не то"}