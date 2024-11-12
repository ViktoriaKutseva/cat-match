import os, sys
sys.dont_write_bytecode = True
sys.path.append(os.getcwd())
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./cats.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

        
# Создаем таблицы, если их еще нет
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("Database and tables created successfully!")