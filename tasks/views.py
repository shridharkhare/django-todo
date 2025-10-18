from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm

def index(request):
    # list + create combined
    tasks = Task.objects.order_by('-created_at')

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:index')
    else:
        form = TaskForm()

    return render(request, 'tasks/index.html', {'tasks': tasks, 'form': form})


def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks:index')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form, 'task': task})


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks:index')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})


def toggle_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    return redirect('tasks:index')
