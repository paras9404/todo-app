from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, TaskSerializer, CommentSerializer
from . import models
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, permission_classes

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class TaskViewSet(viewsets.ModelViewSet):
    queryset = models.Task.objects.all()
    serializer_class = TaskSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    
    
    def create(self, request):
        serializer = TaskSerializer(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data)

  
    def remove_comment(self, request, pk, comment):
        comment = models.Comment.objects.get(pk=comment)
        if comment.delete():
            return Response({'message':'Comment deleted'})
        else:
            return Response({'message':'unable to delete comment'})



