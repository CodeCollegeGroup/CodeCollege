from django.db import models
from django.contrib.auth.models import User

class OrdinaryUser(User):

    university = models.ForeignKey(
        'universities.University',
        related_name='students',
        on_delete=models.SET_NULL,
        null=True
    )

    college_registry = models.CharField(
        max_length=20
    )

    birthday = models.DateField()
    college_registry = models.CharField(max_length=20)

class Profile(models.Model):
    pass
