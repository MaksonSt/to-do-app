from django.conf import settings
from django.db import models



class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True)
    bio = models.TextField(blank=True)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    background_color = models.CharField(max_length=7, default='#ffffff')


    def __str__(self):
        return f"{self.user.first_name}"
