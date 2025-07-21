from django.shortcuts import render, redirect
from django.utils.html import conditional_escape

from .forms import NameChangeForm
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.views.generic import DetailView, UpdateView, ListView, View
from .models import UserProfile
from django.urls import reverse
from .forms import UpdateProfileForm, UserUpdateForm

User = get_user_model()


class UserProfileDetailView(DetailView):
    model = UserProfile
    template_name = 'userprofile/profile.html'
    context_object_name = 'profile'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_authenticated:
            first_name = user.first_name or ''
            last_name = user.last_name or ''
            context["first_name"] = first_name
            context["last_name"] = last_name
        return context



class UserProfileUpdateView(View):
    def get(self, request, pk):
        form1 = UserUpdateForm(instance=request.user)
        form2 = UpdateProfileForm(instance=request.user.userprofile)
        profile = request.user.userprofile
        return render(request, 'userprofile/update_profile.html', {'form1': form1, 'form2': form2, 'profile': profile})

    def post(self, request, pk):
        form1 = UserUpdateForm(request.POST, instance=request.user)
        form2 = UpdateProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            return redirect('user_profile:profile_detail', pk=pk)

        return render(request, 'userprofile/update_profile.html', {'form1': form1, 'form2': form2})


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



