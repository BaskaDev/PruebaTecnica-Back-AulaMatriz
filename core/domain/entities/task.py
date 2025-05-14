from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional


class Priority(Enum):
    BAJA = "baja"
    MEDIA = "media"
    ALTA = "alta"


@dataclass
class Task:
    id: Optional[int]
    titulo: str
    descripcion: Optional[str]
    fecha_creacion: datetime
    fecha_limite: datetime
    prioridad: Priority

    @classmethod
    def create(cls, titulo: str, fecha_limite: datetime, prioridad: Priority, descripcion: Optional[str] = None) -> 'Task':
        return cls(
            id=None,
            titulo=titulo,
            descripcion=descripcion,
            fecha_creacion=datetime.now(),
            fecha_limite=fecha_limite,
            prioridad=prioridad
        ) 