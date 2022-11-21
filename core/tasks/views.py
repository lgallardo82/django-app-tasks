from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Task
from .serializers import TaskSerializer
from rest_framework import status
from rest_framework.decorators import api_view

from rest_framework import generics

# Create your views here.

class CreateNewTask(APIView):
  def post(self, request, format=None):
    newTask = TaskSerializer(data=request.data)
    if newTask.is_valid():
        newTask.save()
        return Response({"msg": "Tarea creada exitosamente"}, status=status.HTTP_201_CREATED)
    return Response(newTask.errors, status=status.HTTP_400_BAD_REQUEST)

class GetAllTasks(APIView):
  def get(self, request):
    print("LLegó un get!!!")
    response = {"msg": "Hola! API online!"}
    tasks= Task.objects.all()
    serializer=TaskSerializer(tasks, many=True)
    print(tasks)
    return Response(serializer.data) 

class GetTaskById(APIView):
  def get(self, request, pk):
    oneTask =Task.objects.get(id=pk)
    serializer=TaskSerializer(oneTask)
    return Response(serializer.data) 

class UpdateTaskById(APIView):
  def put(self, request, pk):
    putTask = Task.objects.get(id=pk)
    serializer = TaskSerializer(putTask, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteTaskById(APIView):
  def delete(self, request, pk, format=None):
    try: 
      deleteTask = Task.objects.get(id=pk)
      deleteTask.delete()
      response = {"msg": "Tarea borrada exitosamente"}
      return Response(response)
    except:
      return Response( {"msg": "Error al borrar registro"}, status=status.HTTP_204_NO_CONTENT)
      

'''class GetTasks(generics.ListAPIView):
  queryset=task.objects.all()
  serializer_class = TaskSerializer'''


class GetTasksByUserIDView(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        queryset = Task.objects.filter(user = user_id)
        return queryset

@api_view(['GET'])
def task_detail(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
        serializer = TaskSerializer(task)
        return Response(serializer.data, status = 200)
    except:

        return Response({"msg": "No existe ninguna tarea con ese ID"}, status = 404)
