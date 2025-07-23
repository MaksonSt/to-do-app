from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = "to_do_app"
urlpatterns = [
    path('', views.home, name='Home'),
    path('task/', views.task_list, name='task-list'),
    path('addtask/', views.add_task, name='add_task'),
    path('complete_task/<int:pk>/', views.complete_task, name='task_complete'),
    path('complete_task_in_list/<int:pk>', views.complete_task_in_list, name='task_complete_in_list'),
    path('delete_task/<int:pk>', views.delete_task, name='delete_task'),
    path('create_tasks_list/', views.create_list_of_tasks, name='create_tasks_list'),
    path('detail_task_list/<int:pk>/', views.add_tasks_in_list, name='add_task_to_list'),
    path('menu_list_task/<int:pk>/',views.menu_list_task, name='menu_list_task'),
    path('update_list_task/<int:pk>/', views.update_task_from_list, name='update_list_task'),
    path('delete_list_task/<int:pk>/', views.delete_task_from_list, name='delete_task_from_list'),
    path('delete_list/<int:pk>', views.delete_list_of_task, name='delete_list'),
    path('about/', views.about, name='about'),
    path('faqs/', views.faqs, name='faqs'),
    path('features/', views.features, name='features'),
    path('update_task/<int:pk>/', views.edit_task, name='update_task'),
    path('search/', views.search_task, name='search_task'),
    path('register/', views.register_user, name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='to_do_app:Home'), name='logout'),
    path('email/', views.send_email, name='email'),
    path('password-reset/', views.password_reset_request, name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='auth/password_reset_done.html'
    ), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='auth/password_reset_confirm.html',
        success_url='/reset/done/'
    ), name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='auth/password_reset_complete.html'
    ), name='password_reset_complete'),


]