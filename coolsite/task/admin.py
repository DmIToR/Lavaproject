from django.contrib import admin

from .models import *
admin.site.register(Task)
admin.site.register(Role)
admin.site.register(User2Task)
#admin.site.register(Box)