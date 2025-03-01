from sqlmodel import SQLModel, Field
from datetime import datetime

class Leyenda(SQLModel, table=True):
    #Modelo de datos que representa una leyenda en la base de datos.
    id: int | None = Field(default=None, primary_key=True)
    image_url: str = Field(nullable=False)  
    name: str = Field(nullable=False, max_length=255)  
    category: str = Field(nullable=False, max_length=100)  
    description: str = Field(nullable=False)  
    created_at: datetime = Field(nullable=False)  
    province: str = Field(nullable=False, max_length=100)  
    canton: str = Field(nullable=False, max_length=100)  
    district: str = Field(nullable=False, max_length=100)  
