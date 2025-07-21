from django.urls import path
from .views import UserProfileDetailView, UserProfileUpdateView


app_name = "user_profile"
urlpatterns = [
    path('<int:pk>/', UserProfileDetailView.as_view(), name='profile_detail'),
    path('update/<int:pk>/', UserProfileUpdateView.as_view(), name='profile_edit')
]