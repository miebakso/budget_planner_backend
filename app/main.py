from fastapi import Depends, FastAPI
from functools import lru_cache
from app.config import settings
from app.routers import categories


app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)

app.include_router(categories.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

