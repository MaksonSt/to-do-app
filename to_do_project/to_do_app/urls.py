from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='Home'),
    path('task/', views.task_list, name='task-list')
]