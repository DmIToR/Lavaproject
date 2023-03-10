from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView


from .forms import *
from .models import *
from django.http import HttpResponseRedirect, Http404

class rols:
    def get_role(self):
        return Role.objects.all()

    def get_user(self):
        return User.objects.all()
    
    def get_tasks(self):
        return Task.objects.all()
    
    def get_User2Task(self):
        return User2Task.objects.all()   


class RegisterUser(CreateView):
    form_class = AddUserForm
    template_name = 'task/html/signup.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form): # если рег успешно, автоматом авторизируем
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'task/html/login.html'
    context_object_name = 'user'

    def get_success_url(self):
        return reverse_lazy('home')


class AddTask(rols, CreateView):
    form_class = AddTaskForm
    template_name = 'task/html/addtask.html'
    #User2Task(id_user = rol, id_role = id_user, id_task = 6).save() # создаст запись в таблице Dealer
    #User2Task.objects.tasks.add(i)
    success_url = reverse_lazy('home')

#def detask(request, task_id): # удаление задачи из бокса
#    Task.objects.get(id=task_id).tasks.remove(task_id)
#    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class delegate(CreateView): # Делегирование задач
    form_class = delegateTaskForm
    template_name = 'task/html/delegate.html'
    success_url = reverse_lazy('home')


class TaskHome(rols, ListView): # Главная страница с задачами
    # paginate_by = 3
    model = Task # Ссылка на модель
    template_name = 'task/html/index.html' # явное указание пути
    context_object_name = 'posts' # собственное имя для обращения к информации
    object_list = User.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs) # сохранение предыдущего контекста
        context['title'] = 'Главная страница'
        return context

def LogoutUser(request):
    logout(request)
    return redirect('login')


class FilterTask(rols, ListView): # Страница с выводом отфильтрованных задач
    template_name = 'task/html/filter.html' # явное указание пути
    context_object_name = 'posts'
    def get_queryset(self):
        queryset = User2Task.objects.filter(
            id_role__in=self.request.GET.getlist("role"), id_user__in=self.request.GET.getlist("user")).distinct("id_task")
        return queryset
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs) # сохранение предыдущего контекста
        context['title'] = 'filter'
        return context
    

def show_task(request, task_id): # подробное описание задачи
    post = get_object_or_404(Task, pk=task_id)
    users = User2Task.objects.filter(id_task=task_id)

    context = {
        'post': post,
        'users': users,        
        'title': post.name,
    }

    return render(request, "task/html/task_page.html", context=context)

    


class Boxing(rols, ListView):
    template_name = 'task/html/box.html' # явное укзание пути
    context_object_name = 'box'
    def get_queryset(self):
        queryset = Box.objects.filter(
            users__in=self.request.GET.getlist("user")
        )
        return queryset
     
    

def updatebox(request, boxid): # добавление задач в бокс
    for i in request.GET.getlist("tasking"):
        Box.objects.get(id=boxid).tasks.add(i)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def debox(request, boxid): # удаление бокса
    Box.objects.filter(id=boxid).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def detask(request, boxid, taskid): # удаление задачи из бокса
    Box.objects.get(id=boxid).tasks.remove(taskid)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class AddBoxes(CreateView): # создание бокса
    form_class = AddBoxForm
    template_name = 'task/html/addbox.html'
    success_url = reverse_lazy('home')