from pydantic import baseSettings

class settings(baseSettings):
    APP_NAME : str
    APP_VERSION : str 
    SECRET_KEY : str

class config:
    env_file = ".env"

settings = Settings()