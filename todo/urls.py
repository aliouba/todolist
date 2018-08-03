from django.urls import path, include, re_path
from todo.views import TodoList,TodoDetail
urlpatterns = [
    path(r'todolist/', TodoList.as_view()),
    re_path(r'todolist/(?P<pk>[0-9]+)/', TodoDetail.as_view()),
]
