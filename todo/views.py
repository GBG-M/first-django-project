
from django.shortcuts import render, redirect
from .models import Todo, username

def todo(request):
    items = Todo.objects.all()
    return render(request, 'todo.html', {'todos': items})
def create_todo(request):
    pass        
def get_todo(request):
    todos = Todo.objects.all()
    method = request.method
    for todo in todos:
         new_todo = {
            'title': todo.title,
            'description': todo.description,
            'completed': todo.completed,
            'priority': todo.priority,
            'created_at': todo.created_at,  }
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        priority = request.POST.get('priority')
        Todo.objects.create(title=title, description=description, priority=priority)
        return redirect('todo:todo')
    return render(request, 'create_todo.html')

