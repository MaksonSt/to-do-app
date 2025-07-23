from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import ListOfTasks
from .forms import ListTasksForm
from to_do_app.models import Task
from to_do_app.forms import TaskForm
from to_do_app.views import login_required_message





@login_required_message(login_url='to_do_app:login')
def menu_list_task(request, pk):
    tasklist = get_object_or_404(ListOfTasks, pk=pk)
    tasks = Task.objects.filter(list=tasklist)
    return render(request, 'todo/menu_task_list.html', {'tasklist': tasklist, 'tasks': tasks})


@login_required_message(login_url='to_do_app:login')
def complete_task_in_list(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.complete = not task.complete
    task.save()
    return redirect('todo_lists:menu_list_task', pk=task.list.pk)


@login_required_message(login_url='to_do_app:login')
def delete_task_from_list(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('todo_lists:menu_list_task', pk=task.list.pk)


@login_required_message(login_url='to_do_app:login')
def delete_list_of_task(request, pk):
    tasklist = get_object_or_404(ListOfTasks, pk=pk)
    tasklist.delete()
    messages.success(request, f'{tasklist.name} list was deleted.')
    return redirect('to_do_app:task-list')


@login_required_message(login_url='to_do_app:login')
def update_task_from_list(request, pk):
    task:Task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('todo_lists:menu_list_task', pk=task.list.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo/update_task.html', {"form": form})


@login_required_message(login_url='to_do_app:login')
def create_list_of_tasks(request):
    if request.method == 'POST':
        form = ListTasksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('to_do_app:task-list')
    else:
        form = ListTasksForm()
    return render(request, 'todo/create_task_list.html', {'form': form})




@login_required_message(login_url='to_do_app:login')
def add_tasks_in_list(request, pk):
    tasklist = get_object_or_404(ListOfTasks, pk=pk)

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.list = tasklist
            task.save()
            messages.success(request, f'You added task: {task.task_name}')
            return redirect('todo_lists:menu_list_task', pk=task.list.pk)
    else:
        form = TaskForm()

    tasks = tasklist.tasks.all()

    return render(request, 'todo/add_task_in_list.html', {
        'tasklist': tasklist,
        'form': form,
        'tasks': tasks,
    })



