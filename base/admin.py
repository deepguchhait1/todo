from django.contrib import admin
from .models import Task

# class Task_Admin(admin.ModelAdmin):

admin.site.register(Task)
# Register your models here.
