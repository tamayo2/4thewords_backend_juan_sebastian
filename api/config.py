from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os
from pydantic import ConfigDict

# Cargar variables del .env solo si no están ya definidas en el entorno
if not os.getenv("DATABASE_URL"):
    load_dotenv()

class Settings(BaseSettings):
    DATABASE_URL: str  

    model_config = ConfigDict(env_file=".env")  

# Instancia de configuración
settings = Settings()

# Comprobación si la variable DATABASE_URL está presente
if not settings.DATABASE_URL:
    raise ValueError("DATABASE_URL no está configurada. Asegurarse de que la variable esté en el archivo .env o en el entorno.")