from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
from app.database import create_db_and_tables, close_db_connection
from fastapi.middleware.cors import CORSMiddleware
import logging
import uvicorn

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("app.log"), logging.StreamHandler()],
)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Context manager asincrono para manejar eventos de inicio y apagado de la aplicacion.

    Eventos:
    - startup: Inicializa la base de datos y las tablas necesarias.
    - shutdown: Cierra la conexion con la base de datos de manera segura.

    Excepciones:
    - Si ocurre un error en la inicializacion o cierre de la base de datos,
      se registra el error y se lanza un HTTPException.
    """
    try:
        logger.info("Iniciando la aplicacion de leyendas...")
        create_db_and_tables()
        logger.info("Base de datos y tablas creadas exitosamente.")
        yield
    except Exception as e:
        logger.error(f"Error al iniciar la aplicacion: {e}")
        raise HTTPException(
            status_code=500, detail="Error al inicializar la aplicacion de leyendas."
        )
    finally:
        try:
            logger.info("Apagando la aplicacion de leyendas...")
            close_db_connection()
            logger.info("Conexion a la base de datos cerrada correctamente.")
        except Exception as e:
            logger.error(f"Error al cerrar la conexion a la base de datos: {e}")
            raise HTTPException(
                status_code=500, detail="Error al cerrar la conexion a la base de datos."
            )
app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from app.routers import leyendas

app.include_router(
    leyendas.router, prefix="/leyendas", tags=["leyendas"]
)

@app.get("/")
def root():
    """
    Ruta raiz de la API.

    Returns:
        dict: Mensaje de bienvenida confirmando que el servidor esta activo.
    """
    return {"message": "FastAPI El Servidor Esta Corriendo Exitosamente"}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8080, reload=True)

