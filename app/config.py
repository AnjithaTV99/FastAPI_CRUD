from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_USERNAME:str
    DB_HOST_NAME:str
    DB_PASSWORD:str
    DB_NAME:str
    DB_PORT:str
    class Config:
        env_file=".env"

settings=Settings()
