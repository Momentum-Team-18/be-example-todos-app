from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Todo
# Create your views here.


def index(request):
    todos = Todo.objects.all()
    return render(request, 'todos/index.html', {'todos': todos})
    # http response that the user sees in browser with html & css


def api_list_todos(request):
    todos = Todo.objects.all()
    serialized_todos = {}
    for todo in todos:
        serialized_todos[todo.id] = todo.name
    # serializing is turning the data into a format that can be rendered as JSON
    return JsonResponse(serialized_todos, status=200)
