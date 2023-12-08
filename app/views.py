from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user
from django.contrib import messages

from .models import Task, RepeatingTask

WEEK_DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def home(request):
    context = {}
    user = get_user(request)
    if user.is_authenticated:
        tasks = Task.objects.filter(user=user).order_by('-date')
        repeating_tasks = RepeatingTask.objects.filter(user=user)
        context['tasks'] = tasks
        context['repeating_tasks'] = repeating_tasks
        # for task in repeating_tasks:
        #     task.days = decode(task.days)
        #     for day in task.days:
        #         day = day[0]

    return render(request, 'home.html', context)


def get_days(post):
    days = []
    for day in WEEK_DAYS:
        if day in post:
            days.append(day)
    return days


def encode(days):
    return ''.join(['1' if day in days else '0' for day in WEEK_DAYS])


def decode(days):
    return [WEEK_DAYS[i] for i, day in enumerate(days) if day == '1']


@login_required
def create_task(request):
    context = {'week_days': WEEK_DAYS}
    user = get_user(request)
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        repeat = get_days(request.POST)
        if repeat:
            repeating_task = RepeatingTask.objects.create(
                user=user,
                title=title,
                description=description,
                days=encode(repeat)
            )
            repeating_task.save()
        else:
            task = Task.objects.create(
                user=user,
                title=title,
                description=description
            )
            task.save()
        messages.success(request, 'Task created successfully')
        return redirect('home')
    return render(request, 'create_task.html', context)


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    messages.success(request, 'Task deleted successfully')
    return redirect('home')


@login_required
def delete_repeating_task(request, task_id):
    task = get_object_or_404(RepeatingTask, id=task_id)
    task.delete()
    messages.success(request, 'Task deleted successfully')
    return redirect('home')


@login_required
def mark_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_completed = not task.is_completed
    task.save()
    return redirect('home')
