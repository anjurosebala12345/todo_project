# Generated by Django 4.2.7 on 2023-11-12 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='priority',
        ),
    ]