from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Task, CustomUser
from .forms import TaskForm, RegistrationForm, ResetPasswordForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, get_user_model
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.urls import reverse
from django.conf import settings

User = get_user_model()

def home(request):
    if request.user.is_authenticated:
        return render(request, 'todo/home_authenticated.html')
    else:
        return render(request, 'todo/home_unauthenticated.html')


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo/task_list.html', {'tasks': tasks})


def add_task(request):
    if request.method == 'POST': # check which method we have in request
        form = TaskForm(request.POST) #in request.POST data which we take from request
        if form.is_valid():
            form.save()
        return redirect('task-list')
    else:
        form = TaskForm()
    return render(request, 'todo/add_task.html', {'form': form})



def complete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.complete = not task.complete
    task.save()
    return redirect('task-list')


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task-list')


def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task-list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo/update_task.html', {'form': form})



def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            login(request, user)
            return redirect('Home')
    else:
        form = RegistrationForm()
    return render(request, 'todo/register.html', {'form': form})


def send_email(request, email):
    send_mail(
        subject= 'Notification',
        message= 'Hello from John',
        from_email= 'johncarterofic@gmail.com',
        recipient_list= [email],
        fail_silently=False
    )



def password_reset_request(request):
    if request.method == "POST":
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                user = None  # Щоб не казати користувачу про існування емейлу

            if user:
                token = default_token_generator.make_token(user)
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                reset_link = request.build_absolute_uri(
                    reverse('password_reset_confirm', kwargs={'uidb64': uid, 'token': token})
                )

                subject = 'Відновлення паролю'
                email_template = 'auth/recovery_email.html'
                email_context = {
                    'user': user,
                    'reset_link': reset_link,
                    'valid_hours': 24,  # наприклад, токен діє 24 години
                }
                email_content = render_to_string(email_template, email_context)

                try:
                    send_mail(
                        subject,
                        '',
                        settings.DEFAULT_FROM_EMAIL,
                        [email],
                        html_message=email_content,
                        fail_silently=False,
                    )
                except Exception as e:
                    print(f"Помилка відправки листа: {e}")

            return redirect('password_reset_done')
    else:
        form = ResetPasswordForm()

    return render(request, 'todo/email_form.html', {'form': form})