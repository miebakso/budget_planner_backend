from fastapi import Depends, FastAPI
from functools import lru_cache
from app.config import settings
from app.routers import categories

# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)

app.include_router(categories.router)

# oauth2_scema = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/")
async def root():
    return {"message": "Hello World"}


# @app.post("/token")
# async def token(form_data: OAuth2PasswordRequestForm = Depends()):
#     return True
