from django.db import models
from django.contrib.auth.models import User


class OrdinaryUser(User, models.Model):

    university = models.ForeignKey(
        'universities.University',
        on_delete=models.CASCADE,
        null=True
    )

    birthday = models.DateField()

    college = models.CharField(max_length=80)

    college_registry = models.CharField(max_length=20)
