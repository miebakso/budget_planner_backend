from fastapi import Depends, FastAPI
from app.config import settings
from functools import lru_cache

# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
print(settings.dict())


app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)


# oauth2_scema = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/")
async def root():
    return {"message": "Hello World"}


# @app.post("/token")
# async def token(form_data: OAuth2PasswordRequestForm = Depends()):
#     return True
