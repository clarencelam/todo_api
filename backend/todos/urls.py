# todos/urls.py
from django.urls import path
from .views import ListTodo, DetailTodo

urlpatterns = [
	path('<int:pk>/', DetailTodo.as_view()), # Each todo is accessed via it's pk Primary Key
	path('', ListTodo.as_view()), # at /api, todos will be listed out
]

