from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    SECRET_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()
