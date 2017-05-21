"""
Views for task api
"""

from django.http.response import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import CoreJSONRenderer
from rest_framework.schemas import SchemaGenerator
from .models import Task, Comment, User
from .serializers import TaskSerializer, CommentSerializer, UserSerializer


# Create your views here.

@api_view(['GET', 'POST'])
def tasks(request):
    """
    Functions for Tasks with no id
    """
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def tasks_by_id(request, task_id):
    """
    Functions for Tasks with an id
    """

    try:
        task = Task.objects.get(pk=task_id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def comments(request):
    """
    Functions for Comments with no id
    """
    if request.method == 'GET':
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def comments_by_id(request, comment_id):
    """
    Functions for Comments with an id
    """

    try:
        comment = Comment.objects.get(pk=comment_id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def comments_by_task_id(request, task_id):
    """
    Get Comments by Task Id
    """

    if request.method == 'GET':
        comments = Comment.objects.filter(task=task_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def users(request):
    """
    Functions for Users with no id
    """

    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def users_by_id(request, user_id):
    """
    Functions for Users with an id
    """

    try:
        user = User.objects.get(pk=user_id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Reponse(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def tasks_by_assignee_id(request, user_id):
    """
    Returns all tasks that user_id is assigned to
    """
    if request.method == 'GET':
        tasks = Task.objects.filter(assignees__pk=user_id)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def tasks_by_created_by_id(request, user_id):
    """
    Returns all tasks that user_id created
    """
    if request.method == 'GET':
        tasks = Task.objects.filter(created_by=user_id)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@renderer_classes([CoreJSONRenderer])
def schema(request):
    """
    Uses schema generator to return schema json
    """
    generator = SchemaGenerator(title='Task API')
    return Response(generator.get_schema())
