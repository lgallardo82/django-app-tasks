from django.urls import path
from .views import *

urlpatterns = [
    path('createNewTask/',createNewTask.as_view()),
    path('getAlltasks/', getAllTasks.as_view()),
    path('getTaskById/<int:pk>/', getTaskById.as_view()),
    path('updateTaskById/<int:pk>/', updateTaskById.as_view()),
    path('deleteTaskById/<int:pk>/', deleteTaskById.as_view()),
]