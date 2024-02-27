from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=[('todo', 'To-Do'), ('in_progress', 'In Progress'), ('completed', 'Completed')])
    deadline = models.DateField()

    def __str__(self):
        return self.title