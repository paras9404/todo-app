from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length = 200)
    updated = models.DateTimeField(auto_now_add =True)
    created = models.DateTimeField(auto_now = True)
    expirDate = models.DateTimeField()

class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    Task = models.ForeignKey(Task,null=True, on_delete=models.SET_NULL)
    updated = models.DateTimeField(auto_now_add =True)
    created = models.DateTimeField(auto_now = True)
    