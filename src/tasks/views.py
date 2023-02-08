from django.shortcuts import render, redirect
from .models import *


def home(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'index.html', context)


def tasks(request, c_id):
    category = Category.objects.get(pk=c_id)
    my_tasks = Tasks.objects.filter(category=category).filter(is_done=False)
    my_category = category.title
    context = {
        'tasks': my_tasks,
        'category': my_category,
    }
    return render(request, 'tasks.html', context)


def description(request, task_id):
    task = Tasks.objects.get(pk=task_id)
    category_id = task.category.id
    context = {
        'task': task,
        'category_id': category_id,
    }
    return render(request, 'description.html', context)


def task_del(request, task_id):
    task = Tasks.objects.get(pk=task_id)
    task.is_done = True
    task.save()
    category = task.category.id
    return redirect(tasks, c_id=category)
