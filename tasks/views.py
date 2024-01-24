from django.shortcuts import render,redirect, get_object_or_404
from .models import Task

def list_tasks(request):
    tasks = Task.objects.all()
    print(tasks)
    return render(request ,'list_tasks.html', {'tasks': tasks})


def create_task(request):
    task = Task(title= request.POST['title'], description = request.POST
    ['description'])
    task.save()
    return redirect('/tasks/')

def delete_task(request, task_id):
    task = get_object_or_404(Task, pk= task_id)
    task.delete()
    print(task_id)
    return redirect('/tasks/')