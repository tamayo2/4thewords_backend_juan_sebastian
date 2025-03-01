import logging
from fastapi import HTTPException, status
from sqlmodel import Session, select
from app.models import Leyenda
from app.schemas import LegendCreate, LegendRead, LegendUpdate

# Configuración del logger
logger = logging.getLogger(__name__)


def create_legend(session: Session, legend_data: LegendCreate) -> LegendRead:
    """
    Crea una nueva leyenda en la base de datos.

    - **session**: Sesión activa de la base de datos.
    - **legend_data**: Datos de la nueva leyenda.
    - **Devuelve**: Leyenda creada.
    """
    try:
        legend = Leyenda(**legend_data.model_dump())
        session.add(legend)
        session.commit()
        session.refresh(legend)
        logger.info(f"Leyenda creada con éxito (ID: {legend.id})")
        return LegendRead.model_validate(legend)
    except Exception as e:
        session.rollback()
        logger.error(f"Error al crear la leyenda: {e}", exc_info=True)
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, "Error interno al crear la leyenda.")


def get_legends(session: Session, skip: int = 0, limit: int = 100) -> list[LegendRead]:
    """
    Obtiene una lista de leyendas paginada.

    - **session**: Sesión activa de la base de datos.
    - **skip**: Número de registros a omitir (paginación).
    - **limit**: Número máximo de registros a devolver.
    - **Devuelve**: Lista de leyendas.
    """
    try:
        legends = session.exec(select(Leyenda).offset(skip).limit(limit)).all()
        logger.info(f"Se obtuvieron {len(legends)} leyendas")
        return [LegendRead.model_validate(legend) for legend in legends]
    except Exception as e:
        logger.error(f"Error al obtener las leyendas: {e}", exc_info=True)
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, "Error interno al obtener las leyendas.")


def get_legend(session: Session, legend_id: int) -> LegendRead:
    """
    Obtiene una leyenda específica por su ID.

    - **session**: Sesión activa de la base de datos.
    - **legend_id**: ID de la leyenda a buscar.
    - **Devuelve**: La leyenda encontrada o un error 404 si no existe.
    """
    try:
        legend = session.exec(select(Leyenda).where(Leyenda.id == legend_id)).scalars().first()
        if not legend:
            logger.warning(f"Leyenda con ID {legend_id} no encontrada")
            raise HTTPException(status.HTTP_404_NOT_FOUND, "Leyenda no encontrada")

        logger.info(f"Leyenda obtenida con éxito (ID: {legend.id})")
        return LegendRead.model_validate(legend)
    except Exception as e:
        logger.error(f"Error al obtener la leyenda con ID {legend_id}: {e}", exc_info=True)
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, "Error interno al obtener la leyenda.")


def update_legend(legend_id: int, legend_data: LegendUpdate, session: Session) -> LegendRead:
    """
    Actualiza una leyenda existente en la base de datos.

    - **session**: Sesión activa de la base de datos.
    - **legend_id**: ID de la leyenda a actualizar.
    - **legend_data**: Datos de actualización.
    - **Devuelve**: La leyenda actualizada o un error 404 si no existe.
    """
    try:
        legend = session.exec(select(Leyenda).where(Leyenda.id == legend_id)).scalars().first()
        if not legend:
            logger.warning(f"Intento de actualizar una leyenda inexistente (ID: {legend_id})")
            raise HTTPException(status.HTTP_404_NOT_FOUND, "Leyenda no encontrada")

        # Aplicamos solo los cambios proporcionados (evita sobrescribir con None)
        update_data = legend_data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(legend, key, value)

        session.commit()
        session.refresh(legend)
        logger.info(f"Leyenda con ID {legend.id} actualizada correctamente")
        return LegendRead.model_validate(legend)
    except Exception as e:
        session.rollback()
        logger.error(f"Error al actualizar la leyenda con ID {legend_id}: {e}", exc_info=True)
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, "Error interno al actualizar la leyenda.")


def delete_legend(legend_id: int, session: Session) -> bool:
    """
    Elimina una leyenda por su ID.

    - **session**: Sesión activa de la base de datos.
    - **legend_id**: ID de la leyenda a eliminar.
    - **Devuelve**: `True` si se eliminó correctamente o lanza un error 404 si no existe.
    """
    try:
        legend = session.exec(select(Leyenda).where(Leyenda.id == legend_id)).scalars().first()
        if not legend:
            logger.warning(f"Intento de eliminar una leyenda inexistente (ID: {legend_id})")
            raise HTTPException(status.HTTP_404_NOT_FOUND, "Leyenda no encontrada")

        session.delete(legend)
        session.commit()
        logger.info(f"Leyenda con ID {legend_id} eliminada correctamente")
        return True
    except Exception as e:
        session.rollback()
        logger.error(f"Error al eliminar la leyenda con ID {legend_id}: {e}", exc_info=True)
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, "Error interno al eliminar la leyenda.")
