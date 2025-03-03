from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os
from pydantic import ConfigDict

if not os.getenv("DATABASE_URL"):
    load_dotenv()

class Settings(BaseSettings):
    DATABASE_URL: str  

    model_config = ConfigDict(env_file=".env")  

settings = Settings()

if not settings.DATABASE_URL:
    raise ValueError("DATABASE_URL no esta configurada. Asegurarse de que la variable este en el archivo .env o en el entorno.")