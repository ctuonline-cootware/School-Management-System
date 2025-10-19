import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://dev_user:cs491@localhost:5432/school_management"
    class Config:
        env_file = ".env"

settings = Settings()