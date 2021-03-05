from django.urls import path

from . import views

urlpatterns = [
    path('', views.todo, name='todos'),
    path('<int:pk>/todos', views.todo_list, name='todo_list'),
    path('todos/<int:id>/completed/', views.completed_todo_list, name='completed_todo_list'),
]