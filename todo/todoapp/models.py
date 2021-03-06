from django.db import models
from django.contrib.auth.models import User


class TodoList(models.Model):
    """
    This class defines the todo list model.

    """
    name = models.CharField(max_length=100, blank=False, unique=True)
    description = models.TextField(max_length=200, blank=False)
    done = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return "{}".format(self.name)
