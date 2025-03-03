import logging
from fastapi import APIRouter, HTTPException, Depends, status
from sqlmodel import Session
from app.database import get_session
from app.schemas import LegendCreate, LegendRead, LegendUpdate
from app.crud.leyendas import (
    create_legend,
    get_legends,
    get_legend,
    update_legend,
    delete_legend,
)

logger = logging.getLogger(__name__)
router = APIRouter(tags=["leyendas"])


@router.post("/", response_model=LegendRead, status_code=status.HTTP_201_CREATED)
def create_new_legend(legend: LegendCreate, session: Session = Depends(get_session)):
    """
    Crea una nueva leyenda en la base de datos.

    - **legend**: Datos de la leyenda a crear.
    - **Devuelve**: La leyenda creada.
    """
    new_legend = create_legend(session, legend)
    logger.info(f"Leyenda creada exitosamente con ID {new_legend.id}")
    return new_legend


@router.get("/", response_model=list[LegendRead], response_model_exclude_unset=True)
def read_legends(session: Session = Depends(get_session)):
    """
    Obtiene todas las leyendas disponibles en la base de datos.

    - **Devuelve**: Lista de leyendas.
    """
    legends = get_legends(session)
    logger.info(f"Se obtuvieron {len(legends)} leyendas")
    return legends


@router.get("/{legend_id}", response_model=LegendRead)
def read_legend(legend_id: int, session: Session = Depends(get_session)):
    """
    Obtiene una leyenda específica por su ID.

    - **legend_id**: ID de la leyenda a buscar.
    - **Devuelve**: La leyenda encontrada o un error 404 si no existe.
    """
    legend = get_legend(session, legend_id)
    if not legend:
        logger.warning(f"Leyenda con ID {legend_id} no encontrada")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Leyenda no encontrada")

    logger.info(f"Leyenda con ID {legend_id} obtenida exitosamente")
    return legend


@router.put("/{legend_id}", response_model=LegendRead)
def update_legend_route(legend_id: int, legend: LegendUpdate, session: Session = Depends(get_session)):
    """
    Actualiza los datos de una leyenda existente.

    - **legend_id**: ID de la leyenda a actualizar.
    - **legend**: Datos actualizados de la leyenda.
    - **Devuelve**: La leyenda actualizada o un error 404 si no existe.
    """
    updated_legend = update_legend(legend_id, legend, session)
    if not updated_legend:
        logger.warning(f"Intento de actualizar leyenda con ID {legend_id}, pero no existe")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Leyenda no encontrada")

    logger.info(f"Leyenda con ID {legend_id} actualizada correctamente")
    return updated_legend


@router.delete("/{legend_id}", response_model=dict, status_code=status.HTTP_200_OK)
def delete_legend_route(legend_id: int, session: Session = Depends(get_session)):
    """
    Elimina una leyenda de la base de datos por su ID.

    - **legend_id**: ID de la leyenda a eliminar.
    - **Devuelve**: Mensaje de éxito o un error 404 si la leyenda no existe.
    """
    success = delete_legend(legend_id, session)
    if not success:
        logger.warning(f"Intento de eliminar leyenda con ID {legend_id}, pero no existe")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Leyenda no encontrada")

    logger.info(f"Leyenda con ID {legend_id} eliminada exitosamente")
    return {"message": "Leyenda eliminada con éxito"}
