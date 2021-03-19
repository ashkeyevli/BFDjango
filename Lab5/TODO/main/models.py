
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
# Create your models here.
from django import forms
from django.contrib.auth.models import PermissionsMixin

from TODO import settings
from django.db import models
from django.contrib.auth.models import AbstractUser




class MainUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = ('user')
        verbose_name_plural = ('users')

class Todos(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Название')

    class Meta:
        verbose_name = 'Лист'
        verbose_name_plural = 'Листы'
    def __str__(self):
        return self.name

class Tasks(models.Model):
    task = models.CharField(max_length=255, null=True, blank=True, verbose_name='Название')
    created_date = models.DateField(verbose_name='Дата создания')
    due_on = models.DateField(verbose_name='Дата оканчания')
    owner = models.ForeignKey(MainUser, on_delete=models.RESTRICT, related_name='owner', verbose_name='Владелец')
    mark = models.BooleanField(verbose_name='Статус')
    todos = models.ForeignKey(Todos, on_delete=models.RESTRICT, related_name='todos', verbose_name='Лист')

    class Meta:
        ordering = ['id']
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'