from sqlmodel import Session, select
from fastapi import HTTPException, status
from app.models import Leyenda
from app.schemas import LegendCreate, LegendRead, LegendUpdate
import logging

logger = logging.getLogger(__name__)

def create_legend(session: Session, legend_data: LegendCreate) -> LegendRead:
    try:

        legend = Leyenda(**legend_data.model_dump())
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

def update_legend(legend_id: int, legend_data: LegendUpdate, session: Session) -> LegendRead | None:
    try:
        legend = session.exec(select(Leyenda).where(Leyenda.id == legend_id)).first()
        if legend:
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
            if legend_data.province is not None:
                legend.province = legend_data.province
            if legend_data.canton is not None:
                legend.canton = legend_data.canton
            if legend_data.district is not None:
                legend.district = legend_data.district

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
