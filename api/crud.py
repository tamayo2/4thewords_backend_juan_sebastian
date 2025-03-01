from sqlmodel import Session, select
from fastapi import HTTPException, status
from api.models import Leyenda
from api.schemas import LegendCreate, LegendRead, LegendUpdate
import logging

# Configuración de logging
logger = logging.getLogger(__name__)

# Función para crear una leyenda
def create_legend(session: Session, legend_data: LegendCreate) -> LegendRead:
    try:
        # Creamos el objeto de la leyenda
        legend = Leyenda(**legend_data.model_dump())  # Usamos .model_dump() para obtener los datos del Pydantic model
        session.add(legend)
        session.commit()
        session.refresh(legend)
        return LegendRead.model_validate(legend)
    except Exception as e:
        session.rollback()
        logger.error(f"Error al crear la leyenda: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al crear la leyenda: {e}"
        )

# Función para obtener todas las leyendas
def get_legends(session: Session, skip: int = 0, limit: int = 100) -> list[LegendRead]:
    try:
        legends = session.exec(select(Leyenda).offset(skip).limit(limit)).all()
        return [LegendRead.model_validate(legend) for legend in legends]
    except Exception as e:
        logger.error(f"Error al obtener las leyendas: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al obtener las leyendas: {e}"
        )

# Función para obtener una leyenda por su ID
def get_legend(session: Session, legend_id: int) -> LegendRead | None:
    try:
        legend = session.exec(select(Leyenda).where(Leyenda.id == legend_id)).first()
        return LegendRead.model_validate(legend) if legend else None
    except Exception as e:
        logger.error(f"Error al obtener la leyenda con ID {legend_id}: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al obtener la leyenda con ID {legend_id}: {e}"
        )

# Función para actualizar una leyenda
def update_legend(legend_id: int, legend_data: LegendUpdate, session: Session) -> LegendRead | None:
    try:
        legend = session.exec(select(Leyenda).where(Leyenda.id == legend_id)).first()
        if legend:
            # Actualizamos los campos manualmente si son proporcionados
            if legend_data.name is not None:
                legend.name = legend_data.name
            if legend_data.description is not None:
                legend.description = legend_data.description
            if legend_data.image_url is not None:
                legend.image_url = legend_data.image_url
            if legend_data.category is not None:
                legend.category = legend_data.category
            if legend_data.created_at is not None:
                legend.created_at = legend_data.created_at
            session.commit()
            session.refresh(legend)
            return LegendRead.model_validate(legend)
        else:
            raise HTTPException(status_code=404, detail="Leyenda no encontrada")
    except Exception as e:
        session.rollback()
        logger.error(f"Error al actualizar la leyenda con ID {legend_id}: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al actualizar la leyenda con ID {legend_id}: {e}"
        )

# Función para eliminar una leyenda
def delete_legend(legend_id: int, session: Session) -> bool:
    try:
        legend = session.exec(select(Leyenda).where(Leyenda.id == legend_id)).first()
        if legend:
            session.delete(legend)
            session.commit()
            return True
        else:
            raise HTTPException(status_code=404, detail="Leyenda no encontrada")
    except Exception as e:
        session.rollback()
        logger.error(f"Error al eliminar la leyenda con ID {legend_id}: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al eliminar la leyenda con ID {legend_id}: {e}"
        )
