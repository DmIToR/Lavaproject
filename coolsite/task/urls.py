from django.urls import path
from .views import *

urlpatterns = [
    path('', TaskHome.as_view(), name='home'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutUser, name='logout'),
    path('filter/', FilterTask.as_view(), name='filter'),
    path('box/', Boxing.as_view(), name='box'),
    path('addtask/', AddTask.as_view(), name='addtask'),
    path('box/delete/<int:boxid>/', debox, name='debox'),
    path('box/detask/<int:boxid>/<int:taskid>/', detask, name='detask'),
    path('box/create/', AddBoxes.as_view(), name='crebox'),
    path('box/createtask/<int:boxid>/', updatebox, name='cretbox'),
]