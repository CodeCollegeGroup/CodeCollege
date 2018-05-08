from django.db import models
from django.contrib.auth.models import User


class OrdinaryUser(User, models.Model):

    colaborated_projects = models.ForeignKey(
        'projects.Project',
        on_delete=models.SET_NULL,
        null=True
    )

    birthday = models.DateField()

    college_registry = models.CharField(max_length=20)
