from django.contrib.auth.models import AbstractUser, Permission
from django.db import models


class User(AbstractUser):
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=88)


class Projects(models.Model):

    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    author_user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_user_id')


class Contributors(models.Model):

    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_id')
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='project_id')
    role = models.CharField(max_length=255)


class Issues(models.Model):

    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    tag = models.CharField(max_length=255)
    priority = models.CharField(max_length=255)
    project_issue_id = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='project_issue_id')
    status = models.CharField(max_length=255)
    author_id = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='author_id')
    assignee_user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assignee_user_id')
    created_time = models.DateTimeField(auto_now_add=True)


class Comments(models.Model):

    author_project_user_id = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='author_project_user_id')
    issue_id = models.ForeignKey(Issues, on_delete=models.CASCADE, related_name='issue_id')
    description = models.CharField(max_length=255)
    created_time = models.DateTimeField(auto_now_add=True)
