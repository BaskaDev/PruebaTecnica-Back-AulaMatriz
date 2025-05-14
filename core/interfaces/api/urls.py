from django.urls import path

from core.interfaces.api.views import (create_task, delete_task, list_tasks,
                                       update_task)

urlpatterns = [
    path('tasks/', create_task, name='create_task'),
    path('tasks/', list_tasks, name='list_tasks'),
    path('tasks/<int:task_id>/', update_task, name='update_task'),
    path('tasks/<int:task_id>/', delete_task, name='delete_task'),
] 