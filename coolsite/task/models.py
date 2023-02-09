from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# class Role(models.Model):
#     role_name = models.CharField(max_length=100, unique=True)

#     def __str__(self):
#         return self.role_name


# class Task(models.Model):
#     name = models.CharField(max_length=200)
#     description = models.TextField(blank=True) # описание, необязательное
#     date_start = models.DateTimeField(auto_now_add=True) # дата начала
#     date_duration = models.IntegerField(blank=True) # продолжительность
#     role = models.ForeignKey('Role', on_delete=models.PROTECT, blank=True) # ответственный
#     responsible = models.ForeignKey(User, on_delete=models.PROTECT, blank=True) # ответственный

#     def __str__(self):  
#         return self.name

# class Box(models.Model): # kanban доска
#     name = models.CharField(max_length=255)
#     tasks = models.ManyToManyField(Task, related_name='tasks')
#     users = models.ManyToManyField(User, related_name='users')

#     def __str__(self):
#         return self.name
    
    
# class Task2Task(models.Model):
#     task_id = models.ForeignKey(Task, on_delete=models.PROTECT, related_name='task_id')
#     subtask_id = models.ForeignKey(Task, on_delete=models.PROTECT, related_name='subtask_id')


class Project(models.Model):
    id_project = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    desc = models.TextField(blank=True, null=True)
    date_start = models.DateField()
    date_duration = models.IntegerField()
    date_end = models.DateField()
    id_task = models.ForeignKey('Task', models.DO_NOTHING, db_column='id_task')

    class Meta:
        managed = False
        db_table = 'project'


class Role(models.Model):
    id_role = models.AutoField(primary_key=True)
    name_role = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'role'
    
    def __str__(self):
        return self.name_role


class Task(models.Model):
    id_task = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    desk = models.TextField(blank=True, null=True)
    date_start = models.DateField()
    date_duration = models.IntegerField()
    date_end = models.DateField()

    class Meta:
        managed = False
        db_table = 'task'

    def __str__(self):
        return self.name


class Task2Task(models.Model):
    id_task = models.ForeignKey(Task, models.DO_NOTHING, db_column='id_task')
    id_subtask = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'task2task'


class User2Project(models.Model):
    id_user = models.ForeignKey(User, models.DO_NOTHING, db_column='id_user')
    id_project = models.ForeignKey(Project, models.DO_NOTHING, db_column='id_project')
    id_role = models.ForeignKey(Role, models.DO_NOTHING, db_column='id_role')

    class Meta:
        managed = False
        db_table = 'user2project'


class User2Task(models.Model):
    id_user = models.ForeignKey(User, models.DO_NOTHING, db_column='id_user')
    id_task = models.ForeignKey(Task, models.DO_NOTHING, db_column='id_task')
    id_role = models.ForeignKey(Role, models.DO_NOTHING, db_column='id_role')

    class Meta:
        managed = False
        db_table = 'user2task'


class Users(models.Model):
    id_user = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'users'

class Box(models.Model): # kanban доска
    name = models.CharField(max_length=255)
    tasks = models.ManyToManyField(Task, related_name='tasks')
    users = models.ManyToManyField(User, related_name='users')

    def __str__(self):
        return self.name
