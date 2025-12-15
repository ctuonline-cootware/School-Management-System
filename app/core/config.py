import os
from typing import Optional
from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(env_path)

class Settings(BaseSettings):
    SECRET_KEY: str = os.getenv("SECRET_KEY", "fallback-dev-key")
    DATABASE_URL: Optional[str] = os.getenv("DATABASE_URL")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
    ALGORITHM: str = "HS256"
    
    # pydantic v2 style setting for env file
    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}

settings = Settings()

