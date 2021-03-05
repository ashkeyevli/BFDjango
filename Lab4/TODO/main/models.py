
from django.db import models

# Create your models here.
from django import forms

from TODO import settings


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
    owner = models.CharField(max_length=255, null=True, blank=True, verbose_name='Владельец')
    mark = models.BooleanField(verbose_name='Статус')
    todos = models.ForeignKey(Todos, on_delete=models.RESTRICT, related_name='todos', verbose_name='Лист')

    class Meta:
        ordering = ['id']
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'