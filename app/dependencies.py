from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator 
from app.config import settings

# Database settings
DB_NAME = settings.DB_NAME
DB_USERNAME = settings.DB_USERNAME
DB_PASSWORD = settings.DB_PASSWORD
DB_ADDRESS = settings.DB_ADDRESS
print(DB_NAME)

DB_URL = f"mariadb+mariadbconnector://{DB_USERNAME}:{DB_PASSWORD}@{DB_ADDRESS}/{DB_NAME}?charset=utf8mb4"

print(DB_URL)

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



async def get_db_connection():
    try:
        session = SessionLocal()
        yield session
    finally:
        session.close()