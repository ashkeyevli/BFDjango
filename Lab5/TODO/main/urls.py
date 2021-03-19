from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from main.views import TasksViewSet, TaskViewSet, ListViewSet
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register('todos', TasksViewSet, basename='main')
router.register('todos', TaskViewSet, basename='main')
router.register('', ListViewSet, basename='main')

urlpatterns = [
      path('login/', obtain_jwt_token)
]
urlpatterns += router.urls
