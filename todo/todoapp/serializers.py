from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from .models import TodoList


class TodoListSerializer(serializers.ModelSerializer):
    """
    Changing data from the database from  complex querysets.
    Serialized data is more readable. 

    """

    class Meta:
        """To serialize fields with the model fields."""
        model = TodoList
        fields = ('id', 'name', 'description', 'done', 'date_created')


class UserSerializer(serializers.ModelSerializer):
    """
    Creating user serializers
    """
    class Meta:
        """
        Serializers for the user fields
        """
        model = User
        fields = ('id','username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        #validating user data
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user
        