from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
from app.database import create_db_and_tables, close_db_connection
from fastapi.middleware.cors import CORSMiddleware
import logging
import uvicorn

# Configuración del logger
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("app.log"), logging.StreamHandler()],
)
logger = logging.getLogger(__name__)

# Definir el ciclo de vida correctamente con asynccontextmanager
@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Context manager asíncrono para manejar eventos de inicio y apagado de la aplicación.

    Eventos:
    - startup: Inicializa la base de datos y las tablas necesarias.
    - shutdown: Cierra la conexión con la base de datos de manera segura.

    Excepciones:
    - Si ocurre un error en la inicialización o cierre de la base de datos, 
      se registra el error y se lanza un HTTPException.
    """
    try:
        logger.info("Iniciando la aplicación de leyendas...")
        create_db_and_tables()  # Crea la base de datos y tablas
        logger.info("Base de datos y tablas creadas exitosamente.")
        yield  # Mantiene la aplicación corriendo
    except Exception as e:
        logger.error(f"Error al iniciar la aplicación: {e}")
        raise HTTPException(
            status_code=500, detail="Error al inicializar la aplicación de leyendas."
        )
    finally:
        # Evento de apagado (shutdown)
        try:
            logger.info("Apagando la aplicación de leyendas...")
            close_db_connection()  # Cierra la conexión a la base de datos
            logger.info("Conexión a la base de datos cerrada correctamente.")
        except Exception as e:
            logger.error(f"Error al cerrar la conexión a la base de datos: {e}")
            raise HTTPException(
                status_code=500, detail="Error al cerrar la conexión a la base de datos."
            )

# Crear la aplicación FastAPI con el ciclo de vida
app = FastAPI(lifespan=lifespan)

# Configurar middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Permitir solicitudes desde el frontend
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)

# Incluir el router de leyendas
from app.routers import leyendas  # Importa el módulo de rutas de leyendas

app.include_router(
    leyendas.router, prefix="/leyendas", tags=["leyendas"]
)

@app.get("/")
def root():
    """
    Ruta raíz de la API.

    Returns:
        dict: Mensaje de bienvenida confirmando que el servidor está activo.
    """
    return {"message": "FastAPI de leyendas funcionando correctamente"}

# Ejecutar el servidor solo si se ejecuta directamente este script.
if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8080, reload=True)

