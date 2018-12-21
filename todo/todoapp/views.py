from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response


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
    authentication_classes = ()
    permission_classes = ()

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

class LoginView(APIView):
    """
        This is the login endpoint class
    """
    permission_classes = ()

    def post(self,  request,):
        """
            Login the user endpoint
        """
        username = request.data.get("username")
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            return Response(
                {
                    "token":user.auth_token.key
                }
            )
        else:
            return Response(
                {
                    "error":"User not found or wrong credentials"
                }
            )
