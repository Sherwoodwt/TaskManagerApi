"""
Models
"""

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    """
    Override user model
    """
    notification_arn = models.CharField(max_length=100, null=True, blank=True)
    is_notifiable = models.BooleanField(default=False)


class DateClass(models.Model):
    """
    Abstract class for created_on and updated_on fields
    """

    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class Task(DateClass):
    """
    Model for a Task
    """
    title = models.CharField(max_length=100)
    description = models.TextField()
    assignees = models.ManyToManyField(User, blank=True)
    due_date = models.DateField()
    created_by = models.ForeignKey(User, related_name='created_by')

class Comment(DateClass):
    """
    Model for a Comment
    """
    task = models.ForeignKey(Task)
    created_by = models.ForeignKey(User)
    text = models.TextField()
