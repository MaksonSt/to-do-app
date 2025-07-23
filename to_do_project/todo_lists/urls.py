from django.urls import path
from . import views



app_name = 'todo_lists'
urlpatterns = [
    path('complete_task_in_list/<int:pk>', views.complete_task_in_list, name='task_complete_in_list'),
    path('create_tasks_list/', views.create_list_of_tasks, name='create_tasks_list'),
    path('add_task_in_list/<int:pk>/', views.add_tasks_in_list, name='add_task_to_list'),
    path('menu_list_task/<int:pk>/', views.menu_list_task, name='menu_list_task'),
    path('update_list_task/<int:pk>/', views.update_task_from_list, name='update_list_task'),
    path('delete_list_task/<int:pk>/', views.delete_task_from_list, name='delete_task_from_list'),
    path('delete_list/<int:pk>', views.delete_list_of_task, name='delete_list'),
]