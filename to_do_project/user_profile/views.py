from django.shortcuts import render, redirect
from .forms import NameChangeForm
from django.contrib.auth import get_user_model
from django.contrib import messages

User = get_user_model()



def change_name(request):
    user = request.user
    if request.method == 'POST':
        form = NameChangeForm(request.POST)
        if form.is_valid():
            user.name = form.cleaned_data['new_name']
            messages.info(request, "The name has been changed.")
            user.save()
            return redirect('to_do_app:Home')
    else:
        form = NameChangeForm(initial={'new_name': user.name})
    return render(request, 'userprofile/profile.html', {'form': form})



