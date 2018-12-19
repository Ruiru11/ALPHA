from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import TodoListSerializer
from .models import TodoList 


class CreateView(generics.ListCreateAPIView):
    """
    This dictates how our todolist api will behave.

    """
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Todolist item."""
        serializer.save()