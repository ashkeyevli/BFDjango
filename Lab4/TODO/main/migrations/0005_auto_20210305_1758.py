# Generated by Django 3.1.6 on 2021-03-05 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210305_1343'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tasks',
            options={'ordering': ['id'], 'verbose_name': 'Задача', 'verbose_name_plural': 'Задачи'},
        ),
    ]
