from django.shortcuts import render, redirect
from .forms import NameChangeForm
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.views.generic import DetailView, UpdateView
from .models import UserProfile
from django.urls import reverse
from .forms import UpdateProfileForm

User = get_user_model()


class UserProfileDetailView(DetailView):
    model = UserProfile
    template_name = 'userprofile/profile.html'
    context_object_name = 'profile'



class UserProfileUpdateView(UpdateView):
    model = UserProfile
    form_class = UpdateProfileForm

    def get_success_url(self):
        return reverse('user_profile:profile_detail', kwargs={'pk': self.object.pk})

# def change_name(request):
#     user = request.user
#     if request.method == 'POST':
#         form = NameChangeForm(request.POST)
#         if form.is_valid():
#             user.name = form.cleaned_data['new_name']
#             messages.info(request, "The name has been changed.")
#             user.save()
#             return redirect('to_do_app:Home')
#     else:
#         form = NameChangeForm(initial={'new_name': user.name})
#     return render(request, 'userprofile/profile.html', {'form': form})



