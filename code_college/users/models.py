from django.db import models
from django.contrib.auth.models import User

class OrdinaryUser(User):

    university = models.ForeignKey(
        'universities.University',
        related_name='students',
        on_delete=models.SET_NULL,
        null=True
    )

    college = models.ForeignKey(
        'universities.University',
        on_delete=models.SET_NULL,
        null=True
    )

    birthday = models.DateField()

    college_registry = models.CharField(max_length=20)


class Profile(models.Model):

    def search_project_owner(self, user_id):
        user = User.objects.get(user_id)
        projects = user.created_projects
        return projects
