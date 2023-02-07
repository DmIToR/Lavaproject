from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User




class Role(models.Model):
    role_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.role_name


class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True) # описание, необязательное
    date_start = models.DateTimeField(auto_now_add=True) # дата начала
    date_duration = models.IntegerField(blank=True) # продолжительность
    role = models.ForeignKey('Role', on_delete=models.PROTECT, blank=True) # ответственный
    responsible = models.ForeignKey(User, on_delete=models.PROTECT, blank=True) # ответственный

    def __str__(self):  
        return self.name

class Box(models.Model): # kanban доска
    name = models.CharField(max_length=255)
    tasks = models.ManyToManyField(Task, related_name='tasks')
    users = models.ManyToManyField(User, related_name='users')

    def __str__(self):
        return self.name
    
    
class Task2Task(models.Model):
    task_id = models.ForeignKey(Task, on_delete=models.PROTECT, related_name='task_id')
    subtask_id = models.ForeignKey(Task, on_delete=models.PROTECT, related_name='subtask_id')
    