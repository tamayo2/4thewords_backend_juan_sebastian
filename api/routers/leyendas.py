from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session
from api.database import get_session
from api.schemas import LegendCreate, LegendRead, LegendUpdate
from api.crud import create_legend, get_legends, get_legend, update_legend, delete_legend
import logging

# Configuración del logger
logger = logging.getLogger(__name__)

router = APIRouter()

# Ruta para crear una nueva leyenda
@router.post("/", response_model=LegendRead)
def create_new_legend(legend: LegendCreate, session: Session = Depends(get_session)):
    try:
        return create_legend(session, legend)
    except HTTPException as e:
        logger.error(f"Error al crear la leyenda: {e.detail}")
        raise e

# Ruta para obtener todas las leyendas
@router.get("/", response_model=list[LegendRead])
def read_legends(session: Session = Depends(get_session)):
    try:
        return get_legends(session)
    except HTTPException as e:
        logger.error(f"Error al obtener las leyendas: {e.detail}")
        raise e

# Ruta para obtener una leyenda específica por ID
@router.get("/{legend_id}", response_model=LegendRead)
def read_legend(legend_id: int, session: Session = Depends(get_session)):
    try:
        legend = get_legend(session, legend_id)
        if legend:
            return legend
        raise HTTPException(status_code=404, detail="Leyenda no encontrada")
    except HTTPException as e:
        logger.error(f"Error al obtener la leyenda con ID {legend_id}: {e.detail}")
        raise e

# Ruta para actualizar una leyenda
@router.put("/{legend_id}", response_model=LegendRead)
def update_legend_route(legend_id: int, legend: LegendUpdate, session: Session = Depends(get_session)):
    try:
        updated_legend = update_legend(legend_id, legend, session)
        if updated_legend:
            return updated_legend
        raise HTTPException(status_code=404, detail="Leyenda no encontrada")
    except HTTPException as e:
        logger.error(f"Error al actualizar la leyenda con ID {legend_id}: {e.detail}")
        raise e

# Ruta para eliminar una leyenda
@router.delete("/{legend_id}", response_model=dict)
def delete_legend_route(legend_id: int, session: Session = Depends(get_session)):
    try:
        success = delete_legend(legend_id, session)
        if success:
            return {"message": "Leyenda eliminada con éxito"}
        raise HTTPException(status_code=404, detail="Leyenda no encontrada")
    except HTTPException as e:
        logger.error(f"Error al eliminar la leyenda con ID {legend_id}: {e.detail}")
        raise e
