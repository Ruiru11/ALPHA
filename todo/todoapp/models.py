from django.db import models

class TodoList(models.Model):
    """
    This class defines the todo list model.

    """
    name = models.CharField(max_length=100, blank=False, unique=True)
    description = models.TextField(max_length=200, blank=False)
    done = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return "{}".format(self.name)
