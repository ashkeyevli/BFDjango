# Generated by Django 3.1.6 on 2021-03-05 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='tasks',
            name='due_on',
        ),
    ]
