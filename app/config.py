from pydantic import BaseSettings

# import os
# from dotenv import load_dotenv

# from pathlib import Path
# env_path = Path('.') / '.env'
# load_dotenv(dotenv_path=env_path)

class Settings(BaseSettings):
    PROJECT_NAME: str 
    PROJECT_VERSION: str 
    TEST:str

    class Config:
        env_file = '.env'

# Overide settings for a new .env file
# settings = Settings(_env_file=None)
settings = Settings()
