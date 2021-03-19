from django.shortcuts import render
from .models import Todos, Tasks, MainUser
from rest_framework import generics, mixins, viewsets
from main.serializers import TodosSerializer, TaskSerializer, MainUserSerializer, TasksSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
# # Create your views here.

class TasksViewSet(generics.ListAPIView, generics.UpdateAPIView, generics.DestroyAPIView, viewsets.ViewSet):
    permission_classes = (IsAuthenticated)
    serializer_class = TasksSerializer
    queryset = Tasks.objects.all()

    def get_queryset(self):
        return Tasks.objects.filter(mark=False)

    def get_permissions(self):
        permission_classes = (IsAuthenticated,)
        return [permission() for permission in permission_classes]


    @action(methods=['GET'], detail=True, url_path='completed', url_name='active')
    def active(self, request, pk):
        queryset = Tasks.objects.filter(todos_id=pk, mark=True)
        serializer = TasksSerializer(queryset, many=True)
        return Response(serializer.data)


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated)
    serializer_class = TaskSerializer
    queryset = Tasks.objects.all()
    def get_permissions(self):
        permission_classes = (IsAuthenticated,)
        return [permission() for permission in permission_classes]


class ListViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated)
    serializer_class = TodosSerializer
    queryset = Todos.objects.all()
    def get_permissions(self):
        permission_classes = (IsAuthenticated,)
        return [permission() for permission in permission_classes]

