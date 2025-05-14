from datetime import datetime
from typing import List, Optional

from core.domain.entities.task import Priority, Task
from core.domain.ports.task_repository import TaskRepository


class TaskUseCases:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    def create_task(self, titulo: str, fecha_limite: datetime, prioridad: Priority, descripcion: Optional[str] = None) -> Task:
        task = Task.create(titulo, fecha_limite, prioridad, descripcion)
        return self.task_repository.save(task)

    def get_task(self, task_id: int) -> Optional[Task]:
        return self.task_repository.get_by_id(task_id)

    def get_all_tasks(self) -> List[Task]:
        return self.task_repository.get_all()

    def update_task(self, task_id: int, titulo: str, fecha_limite: datetime, prioridad: Priority, descripcion: Optional[str] = None) -> Optional[Task]:
        task = self.task_repository.get_by_id(task_id)
        if task:
            task.titulo = titulo
            task.fecha_limite = fecha_limite
            task.prioridad = prioridad
            task.descripcion = descripcion
            return self.task_repository.update(task)
        return None

    def delete_task(self, task_id: int) -> bool:
        task = self.task_repository.get_by_id(task_id)
        if task:
            self.task_repository.delete(task_id)
            return True
        return False 