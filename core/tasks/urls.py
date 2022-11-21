from django.urls import path
from .views import *

urlpatterns = [
    path('createNewTask/',CreateNewTask.as_view()),
    path('getAlltasks/', GetAllTasks.as_view()),
    path('getTaskById/<int:pk>/', GetTaskById.as_view()),
    path('updateTaskById/<int:pk>/', UpdateTaskById.as_view()),
    path('deleteTaskById/<int:pk>/', DeleteTaskById.as_view()),
    path('my-tasks', GetTasksByUserIDView.as_view()),
    path('details/<int:task_id>/', task_detail)
]