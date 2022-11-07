from django.contrib import admin
from .models import Priority
from .models import Task

# Register your models here.
admin.site.register(Priority)
admin.site.register(Task)