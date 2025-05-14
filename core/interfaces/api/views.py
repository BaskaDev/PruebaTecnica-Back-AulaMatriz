from typing import List

from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.application.use_cases.task_use_cases import TaskUseCases
from core.domain.entities.task import Priority
from core.infrastructure.repositories.django_task_repository import \
    DjangoTaskRepository
from core.interfaces.api.serializers import TaskCreate, TaskResponse


@api_view(['POST'])
def create_task(request):
    serializer = TaskCreate(data=request.data)
    if serializer.is_valid():
        task_use_cases = TaskUseCases(DjangoTaskRepository())
        task = task_use_cases.create_task(
            titulo=serializer.validated_data['titulo'],
            fecha_limite=serializer.validated_data['fecha_limite'],
            prioridad=serializer.validated_data['prioridad'],
            descripcion=serializer.validated_data.get('descripcion')
        )
        return Response(TaskResponse.from_orm(task), status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_tasks(request):
    task_use_cases = TaskUseCases(DjangoTaskRepository())
    tasks = task_use_cases.get_all_tasks()
    return Response([TaskResponse.from_orm(task) for task in tasks])


@api_view(['PUT'])
def update_task(request, task_id):
    serializer = TaskCreate(data=request.data)
    if serializer.is_valid():
        task_use_cases = TaskUseCases(DjangoTaskRepository())
        task = task_use_cases.update_task(
            task_id=task_id,
            titulo=serializer.validated_data['titulo'],
            fecha_limite=serializer.validated_data['fecha_limite'],
            prioridad=serializer.validated_data['prioridad'],
            descripcion=serializer.validated_data.get('descripcion')
        )
        if task:
            return Response(TaskResponse.from_orm(task))
        raise Http404("Task not found")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_task(request, task_id):
    task_use_cases = TaskUseCases(DjangoTaskRepository())
    if task_use_cases.delete_task(task_id):
        return Response(status=status.HTTP_204_NO_CONTENT)
    raise Http404("Task not found") 