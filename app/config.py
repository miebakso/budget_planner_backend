from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str 
    PROJECT_VERSION: str 
    DB_NAME:str
    DB_USERNAME:str
    DB_PASSWORD:str
    DB_ADDRESS:str


    class Config:
        env_file = '.env'

# Overide settings for a new .env file
# settings = Settings(_env_file=None)
settings = Settings()
