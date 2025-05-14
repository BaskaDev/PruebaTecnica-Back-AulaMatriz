from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from core.domain.entities.task import Priority


class TaskCreate(BaseModel):
    titulo: str = Field(..., max_length=200)
    descripcion: Optional[str] = None
    fecha_limite: datetime
    prioridad: Priority


class TaskResponse(BaseModel):
    id: int
    titulo: str
    descripcion: Optional[str]
    fecha_creacion: datetime
    fecha_limite: datetime
    prioridad: Priority

    class Config:
        from_attributes = True 