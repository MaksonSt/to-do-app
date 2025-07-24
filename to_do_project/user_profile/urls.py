from django.urls import path
from .views import UserProfileDetailView, UserProfileUpdateView
from django.contrib.auth.decorators import login_required


app_name = "user_profile"
urlpatterns = [
    path('<int:pk>/', login_required(UserProfileDetailView.as_view()), name='profile_detail'),
    path('update/<int:pk>/', login_required(UserProfileUpdateView.as_view()), name='profile_edit')
]