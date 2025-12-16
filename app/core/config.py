import os
from typing import Optional
from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# try app/.env first, then project root .env
_here = Path(__file__).resolve()
env_path_app = _here.parents[1] / ".env"      # app/.env
env_path_root = _here.parents[2] / ".env"     # project_root/.env

if env_path_app.exists():
    load_dotenv(env_path_app)
elif env_path_root.exists():
    load_dotenv(env_path_root)
else:
    # fallback: rely on default behavior (no-op) so env vars from the environment are still used
    load_dotenv()

class Settings(BaseSettings):
    SECRET_KEY: str = os.getenv("SECRET_KEY", "fallback-dev-key")
    DATABASE_URL: Optional[str] = os.getenv("DATABASE_URL")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
    ALGORITHM: str = "HS256"
    
    # pydantic v2 style setting for env file
    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}

settings = Settings()

