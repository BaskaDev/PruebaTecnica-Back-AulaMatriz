from typing import List, Optional

from core.domain.entities.task import Priority, Task
from core.domain.ports.task_repository import TaskRepository
from core.infrastructure.models import TaskModel


class DjangoTaskRepository(TaskRepository):
    def save(self, task: Task) -> Task:
        task_model = TaskModel.objects.create(
            titulo=task.titulo,
            descripcion=task.descripcion,
            fecha_limite=task.fecha_limite,
            prioridad=task.prioridad.value
        )
        return self._to_domain(task_model)

    def get_by_id(self, task_id: int) -> Optional[Task]:
        try:
            task_model = TaskModel.objects.get(id=task_id)
            return self._to_domain(task_model)
        except TaskModel.DoesNotExist:
            return None

    def get_all(self) -> List[Task]:
        return [self._to_domain(task_model) for task_model in TaskModel.objects.all()]

    def update(self, task: Task) -> Task:
        task_model = TaskModel.objects.get(id=task.id)
        task_model.titulo = task.titulo
        task_model.descripcion = task.descripcion
        task_model.fecha_limite = task.fecha_limite
        task_model.prioridad = task.prioridad.value
        task_model.save()
        return self._to_domain(task_model)

    def delete(self, task_id: int) -> None:
        TaskModel.objects.filter(id=task_id).delete()

    def _to_domain(self, task_model: TaskModel) -> Task:
        return Task(
            id=task_model.id,
            titulo=task_model.titulo,
            descripcion=task_model.descripcion,
            fecha_creacion=task_model.fecha_creacion,
            fecha_limite=task_model.fecha_limite,
            prioridad=Priority(task_model.prioridad)
        ) 