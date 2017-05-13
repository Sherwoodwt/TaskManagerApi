"""
Serializers
"""

from rest_framework import serializers
from .models import Task, Comment

class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for Task Model
    """
    class Meta:
        model = Task
        fields = (
            'id',
            'created_on',
            'updated_on',
            'title',
            'description',
            'assignees',
            'due_date',
            'created_by',
        )

class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for Comment Model
    """
    class Meta:
        model = Comment
        fields = (
            'id',
            'created_on',
            'updated_on',
            'task',
            'created_by',
            'text',
        )
