from sqlmodel import SQLModel, create_engine, Session
from app.config import settings
import logging

# Configuración del logger para registrar eventos y errores
logger = logging.getLogger(__name__)

# Crear el motor de la base de datos con SQLAlchemy
# 'echo=True' habilita el logging de las consultas SQL en la consola (útil para depuración)
engine = create_engine(settings.DATABASE_URL, echo=True)

def get_session():
    """
    Generador de sesiones de base de datos.

    Utiliza `Session(engine)` para manejar la conexión con la base de datos
    y proporciona una sesión en cada llamada.

    Yields:
        Session: Sesión activa de la base de datos.
    """
    with Session(engine) as session:
        yield session

def create_db_and_tables():
    """
    Crea las tablas en la base de datos basadas en los modelos de SQLModel.

    Si las tablas ya existen, no se sobrescriben. Esta función se debe ejecutar
    en el arranque de la aplicación para garantizar que la base de datos tenga
    la estructura correcta.

    """
    try:
        SQLModel.metadata.create_all(engine)
        logger.info("Las tablas han sido creadas correctamente en la base de datos.")
    except Exception as e:
        logger.error(f"Error al crear las tablas: {e}")
        raise RuntimeError("Error al crear las tablas de la base de datos.")

def close_db_connection():
    """
    Cierra la conexión con la base de datos.
    """
    try:
        logger.info("Cerrando conexión con la base de datos...")
    except Exception as e:
        logger.error(f"Error al cerrar la conexión con la base de datos: {e}")
