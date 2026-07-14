# from django.shortcuts import render

# # Create your views here.


from django.shortcuts import render, redirect
from .models import Task

# Show all tasks
# def task_list(request):
#     tasks = Task.objects.all()             # fetch all rows from SQLite3
#     return render(request, 'todo/list.html', {'tasks': tasks})

def task_list(request):
    tasks = Task.objects.all()
    completed_count = Task.objects.filter(completed=True).count()
    pending_count = Task.objects.filter(completed=False).count()
    return render(request, 'todo/list.html', {
        'tasks': tasks,
        'completed_count': completed_count,
        'pending_count': pending_count,
    })


# Add a new task
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        Task.objects.create(title=title)   # save to SQLite3
        return redirect('task_list')
    return render(request, 'todo/add.html')

# Mark task as complete
def complete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.completed = True
    task.save()
    return redirect('task_list')

# Delete a task
def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('task_list')