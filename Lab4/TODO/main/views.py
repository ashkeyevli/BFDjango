from django.shortcuts import render
from .models import Todos, Tasks
# Create your views here.

def todo_list(request, pk):
    tasks = Tasks.objects.filter(todos=pk, mark=False)
    todos = Todos.objects.get(id=pk)
    context = {   'tasks_list': tasks,
                  'todo': todos
         }
    return render(request, 'todo_list.html', context)

def completed_todo_list(request, id):
    tasks = Tasks.objects.filter(todos=id, mark=True)
    todos = Todos.objects.get(id=id)
    context = {'tasks_list': tasks,
               'todo': todos,

               }
    return render(request, 'completed_todo_list.html', context)

def todo(request):
    todos = Todos.objects.all()
    context = {   'todos': todos }
    return render(request, 'todos.html', context)