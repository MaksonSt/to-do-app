from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm


def home(request):
    return render(request, 'todo/home.html')



def task_list(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'todo/task_list.html', context)


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('task_list')



def complete_task(request):
    pass