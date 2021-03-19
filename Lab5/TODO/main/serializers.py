from rest_framework import serializers
from main.models import Tasks, Todos, MainUser


class TodosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todos
        fields = '__all__'


class TasksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tasks
        fields = ('id', 'task', 'mark', 'todos')


class MainUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = MainUser
        fields = ('id', 'username', 'first_name', 'email', 'bio')


class TaskSerializer(serializers.ModelSerializer):
    todos = TodosSerializer()
    owner = MainUserSerializer()
    class Meta:
        model = Tasks
        fields = ('id', 'created_date', 'due_on', 'owner', 'todos', 'task', 'mark')

