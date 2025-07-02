from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.home, name='Home'),
    path('task/', views.task_list, name='task-list'),
    path('addtask/', views.add_task, name='add_task'),
    path('complete_task/<int:pk>/', views.complete_task, name='task_complete'),
    path('delete_task/<int:pk>', views.delete_task, name='delete_task'),
    path('update_task/<int:pk>/', views.edit_task, name='update_task'),
    path('register/', views.register_user, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='todo/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='Home'), name='logout'),
    path('email/', views.send_email, name='email'),
    path('password-reset/', views.password_reset_request, name='password_reset'),
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