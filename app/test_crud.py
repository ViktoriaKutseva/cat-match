from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base
from models.cat import Cat
from services.crud import create_cat, delete_cat, get_cats
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def test_crud():
    db = SessionLocal()

    cat = create_cat(db, "Клевер", 3, "Охуенная")
    print(f"Создана кошка: {cat.name}, ID: {cat.id}")

    cat = create_cat(db, "Рысечка", 6, "Пухлая")
    print(f"Создана кошка: {cat.name}, ID: {cat.id}")

    cats = get_cats(db)
    print('Список кошек в базе данных')
    for c in cats:
        print(f"{c.id}: {c.name}, {c.age} лет, порода: {c.breed}")
    
    deleted_cat = delete_cat(db, cat.id)
    if delete_cat:
        print(f"Удалена кошка: {deleted_cat.name}, ID: {deleted_cat.id}")
    else:
        print("Кошка не найдена для удаления.")

    remaining_cats = get_cats(db)
    print("Оставшиеся кошки в базе данных:")
    for c in remaining_cats:
        print(f"{c.id}: {c.name}, {c.age} лет, порода: {c.breed}")

    db.close()


 if __name__ == "__main__":
    test_crud()