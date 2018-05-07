from django.db import models
from django.contrib.auth.models import User
from comments.migrations import Rating

class OrdinaryUser(User, models.Model):

    birthday = models.DateField()

    college_registry = models.CharField(max_length=20)

class Profile(models.Model):

    def search_project_owner(self, user_id):
        user = User.objects.get(user_id)
        projects = user.created_projects
        return projects