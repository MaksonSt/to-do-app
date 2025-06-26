from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def home(request):
    return render(request, 'todo/home.html', )


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
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            login(request, user)
            return redirect('Home')
    else:
        form = UserCreationForm()
    return render(request, 'todo/register.html', {'form': form})