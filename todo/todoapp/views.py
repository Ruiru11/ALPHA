from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
from rest_framework import generics
from .serializers import TodoListSerializer, UserSerializer
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

class UserCreate(generics.ListCreateAPIView):
    """
    Handles user POST and GET requests

    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

    def perform_create(self, serializer):
        """Save the post data when creating a new user."""
        serializer.save()


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles PUT, GET and DELETE requests

    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class ToDoDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """
    Class handles getting a single product, editing the product and deleting the product
    """

    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
