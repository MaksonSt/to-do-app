from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Task, CustomUser, Tags
from .forms import TaskForm, RegistrationForm, ResetPasswordForm, TaskSearchForm, LoginForm
from todo_lists.models import ListOfTasks
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, get_user_model
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.urls import reverse
from django.conf import settings
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

User = get_user_model()


def login_required_message(function=None, login_url=None):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                messages.info(request, "Будь ласка, зареєструйтесь або увійдіть, щоб продовжити.")
                return redirect(login_url or 'login')
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    if function:
        return decorator(function)
    return decorator



def home(request):
    if request.user.is_authenticated:
        return render(request, 'todo/home_authenticated.html')
    else:
        return render(request, 'todo/home_unauthenticated.html')


@login_required_message(login_url='to_do_app:login')
def task_list(request):
    tasks = Task.objects.filter(list__isnull=True, user=request.user)
    tasklists = ListOfTasks.objects.filter(user=request.user)
    form = TaskSearchForm(request.GET or None)
    all_tags = Tags.objects.all()

    FILTER_MAPPING = {
        'done': lambda queryset: queryset.filter(complete=True),
        'undone': lambda queryset: queryset.filter(complete=False),
        'tags': lambda queryset, value: queryset.filter(tags__name=value)
    }

    SORT_MAPPING = {
        'done': lambda queryset: queryset.order_by('-complete'),
        'undone': lambda queryset: queryset.order_by('complete'),
        'data_added': lambda queryset: queryset.order_by('data_added'),
        'alphabet': lambda queryset: queryset.order_by('-task_name')
    }

    sort_param = request.GET.get('sort')
    filter_param = request.GET.get('filters')

    if request.GET:

        # sorting
        if sort_param in SORT_MAPPING:
            tasks = SORT_MAPPING[sort_param](tasks)

        #filters
        if filter_param in FILTER_MAPPING:
            if filter_param == 'tags':
                tag_value = request.GET.get('tag')
                if tag_value:
                    tasks = FILTER_MAPPING['tags'](tasks, tag_value)
            else:
                tasks = FILTER_MAPPING[filter_param](tasks)

        #searching
        if form.is_valid():
            query = form.cleaned_data.get('query')
            if query:
                tasks = tasks.filter(Q(task_name__icontains=query) | Q(description__icontains=query))


    context = {
            'form' : form,
            'tasks' : tasks,
            'tasklists' : tasklists,
            'all_tags': all_tags
        }

    return render(request, 'todo/task_list.html', context)




@login_required_message(login_url='to_do_app:login')
def add_task(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        task = form.save(commit=False)
        task.user = request.user
        task.save()
        form.save_m2m()
        return redirect('to_do_app:task-list')
    return render(request, 'todo/add_task.html', {'form': form})


@login_required_message(login_url='to_do_app:login')
def complete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.complete = not task.complete
    task.save()
    return redirect('to_do_app:task-list')




@login_required_message(login_url='to_do_app:login')
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('to_do_app:task-list')


@login_required_message(login_url='to_do_app:login')
def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('to_do_app:task-list')
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
            messages.success(request, f'You successfully register. Welcome {user.first_name}!', )
            return redirect('to_do_app:Home')
    else:
        form = RegistrationForm()
    return render(request, 'todo/register.html', {'form': form})


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'todo/login.html'
    authentication_form = LoginForm
    success_url = reverse_lazy(settings.LOGIN_REDIRECT_URL)
    success_message = "You successfully Login! Welcome!"


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
                    reverse('to_do_app:password_reset_confirm', kwargs={'uidb64': uid, 'token': token})
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

            return redirect('to_do_app:password_reset_done')
    else:
        form = ResetPasswordForm()

    return render(request, 'todo/email_form.html', {'form': form})





def about(request):
    return render(request, "todo/about.html")


def faqs(request):
    return render(request, "todo/faqs.html")


def features(request):
    return render(request, "todo/features.html")

