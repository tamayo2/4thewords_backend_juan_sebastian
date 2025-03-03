from sqlmodel import SQLModel
from datetime import datetime
from pydantic import ConfigDict

class LegendCreate(SQLModel):
    image_url: str
    name: str
    category: str
    description: str
    created_at: datetime  
    province: str  
    canton: str    
    district: str  

class LegendRead(SQLModel):
    id: int  
    image_url: str
    name: str
    category: str
    description: str
    created_at: datetime  
    province: str  
    canton: str    
    district: str  

class LegendUpdate(SQLModel):
    image_url: str | None = None  
    name: str | None = None
    category: str | None = None
    description: str | None = None
    created_at: datetime | None = None  
    province: str  | None = None
    canton: str    | None = None
    district: str  | None = None

    model_config = ConfigDict(from_attributes=True)