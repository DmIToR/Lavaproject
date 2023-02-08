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
    class Meta:
        model = Task
        fields = '__all__'

class AddBoxForm(forms.ModelForm):
    class Meta:
        model = Box
        fields = '__all__'