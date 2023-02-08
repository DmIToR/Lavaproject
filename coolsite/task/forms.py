from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import *
from django.contrib.auth.models import User


class AddUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput())
    email = forms.EmailField(label="email", widget=forms.EmailInput())
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput())

    class Meta:
        model = User # Связь формы с моделью
        fields = ('username', 'email', 'password1', 'password2') # показывает какие поля берем из модели


class AddTaskForm(forms.ModelForm):
    name = forms.CharField(label='Название задачи:', widget=forms.TextInput())
    desk = forms.CharField(label='Описание задачи:', widget=forms.Textarea())
    date_start = forms.DateField(label='Дата начала:', initial = timezone.now().date())
    date_duration = forms.IntegerField(label='Продолжительность:')
    date_end = forms.DateField(label = 'Дата окончания:', initial = timezone.now().date())


    user_choices = [(user.id, user.username) for user in AuthUser.objects.all()]
    selected_user = forms.MultipleChoiceField(choices=user_choices, label = "Ответственный")

    class Meta:
        model = Task
        fields = ('id_task','name', 'desk', 'date_start', 'date_duration', 'date_end')

class AddBoxForm(forms.ModelForm):
    class Meta:
        model = Box
        fields = '__all__'
# 32 строчка index 	<!--<a href="{% url 'box' %}?user={{user.id}}">Боксы</a>--> почему-то с ним не работает