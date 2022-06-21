from rest_framework import  serializers
from django.contrib.auth.models import User
from .models import Task, Comment

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_staff']


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = [ 'content', 'user']


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    # Comment = CommentSerializer(read_only=True)
    class Meta:
        model = Task
        fields = ['url','title','user', 'description']
    