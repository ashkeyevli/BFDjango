# Generated by Django 3.1.6 on 2021-03-05 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210305_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='created_date',
            field=models.DateField(verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='due_on',
            field=models.DateField(verbose_name='Дата оканчания'),
        ),
    ]
