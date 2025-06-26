from django.contrib import admin
from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_name', 'description', 'data_added', 'complete')


