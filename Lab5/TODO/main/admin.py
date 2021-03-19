from django.contrib import admin
from main.models import Todos, Tasks, MainUser
@admin.register(Todos)
class TodosAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['id']
    search_fields = ['name']

@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ['task', 'created_date', 'due_on', 'owner', 'mark', 'todos']
    ordering = ['id']
    search_fields = ['task', 'owner', 'mark', 'todos__name']
    list_filter = ['created_date', 'due_on', 'owner', 'mark', 'todos__name']

admin.site.register(MainUser)