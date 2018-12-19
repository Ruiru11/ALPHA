from rest_framework import serializers
from .models import TodoList


class TodoListSerializer(serializers.ModelSerializer):
    """
    Changing data from the database from  complex querysets.
    Serialized data is more readable. 

    """

    class Meta:
        """To serialize fields with the model fields."""
        model = TodoList
        fields = ('id', 'name', 'description', 'done' 'date_created')
        read_only_fields = ('date_created')