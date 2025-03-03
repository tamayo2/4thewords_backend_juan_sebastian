from sqlmodel import SQLModel, Field
from datetime import datetime

class Leyenda(SQLModel, table=True):
    """
    Modelo de datos que representa una leyenda en la base de datos.
    """

    id: int | None = Field(default=None, primary_key=True, title="ID de la Leyenda")
    image_url: str = Field(title="URL de la imagen", max_length=500)
    name: str = Field(title="Nombre de la Leyenda", max_length=255)
    category: str = Field(title="Categoria", max_length=100)
    description: str = Field(title="Descripcion de la Leyenda")
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        title="Fecha de Creacion",
        description="Fecha en la que se creo la leyenda"
    )
    province: str = Field(title="Provincia", max_length=100)
    canton: str = Field(title="Canton", max_length=100)
    district: str = Field(title="Distrito", max_length=100)
