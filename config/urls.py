"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from todos import views

user_list = views.UserViewSet.as_view({
    'get': 'list',
})
user_detail = views.UserViewSet.as_view({
    'get': 'retrieve',
})
todo_list = views.TodoViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
todo_detail = views.TodoViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="home"),
    path('accounts/', include('registration.backends.simple.urls')),
    # path('api/todos', views.api_list_todos, name="api-todos"),
    path('api/users', user_list, name='user-list'),
    path('api/users/<int:pk>', user_detail, name='user=detail'),
    path('api/todos', todo_list, name='todo-list'),
    # updates line 43 to use drf
    path('api/todos/<int:pk>', todo_detail, name='todo-detail'),
]
