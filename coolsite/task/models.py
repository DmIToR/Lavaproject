# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from datetime import datetime
from django.utils import timezone


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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


class Task2Task(models.Model):
    id_task = models.ForeignKey(Task, models.DO_NOTHING, db_column='id_task')
    id_subtask = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'task2task'


class TaskBox(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'task_box'


class TaskBoxTasks(models.Model):
    id = models.BigAutoField(primary_key=True)
    box = models.ForeignKey(TaskBox, models.DO_NOTHING)
    task = models.ForeignKey(Task, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'task_box_tasks'
        unique_together = (('box', 'task'),)


class TaskBoxUsers(models.Model):
    id = models.BigAutoField(primary_key=True)
    box = models.ForeignKey(TaskBox, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'task_box_users'
        unique_together = (('box', 'user'),)


class User2Project(models.Model):
    id_user = models.ForeignKey('Users', models.DO_NOTHING, db_column='id_user')
    id_project = models.ForeignKey(Project, models.DO_NOTHING, db_column='id_project')
    id_role = models.ForeignKey(Role, models.DO_NOTHING, db_column='id_role')

    class Meta:
        managed = False
        db_table = 'user2project'


class User2Task(models.Model):
    id_user = models.ForeignKey('Users', models.DO_NOTHING, db_column='id_user')
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
    users = models.ManyToManyField(Users, related_name='users')

    def __str__(self):
        return self.name