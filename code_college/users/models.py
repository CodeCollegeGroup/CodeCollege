from django.db import models
from django.contrib.auth.models import User
from universities.models import University


class OrdinaryUser(User):

    colaborated_projects = models.ForeignKey(
        'projects.Project',
        on_delete=models.SET_NULL,
        null=True
    )

    birthday = models.DateField()

    college_registry = models.CharField(max_length=20)

    university = models.ForeignKey(
        'universities.University',
        on_delete=models.DO_NOTHING,
        related_name='students'
    )
