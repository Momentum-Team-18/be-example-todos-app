from rest_framework import viewsets
from django.http import JsonResponse
from django.shortcuts import render
from .models import Todo, User
from .serializers import UserSerializer, TodoSerializer


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


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    This viewset allows for listing and retrieving User instances
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TodoViewSet(viewsets.ModelViewSet):
    '''
    This viewset provides 'list', 'create', 'retrieve', 'update', and 'destroy' actions for instances of the model Todo
    '''
    serializer_class = TodoSerializer

    def get_queryset(self):
        return self.request.user.todos.all()
