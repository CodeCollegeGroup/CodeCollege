from django.db import models
from django.contrib.auth.models import User


class OrdinaryUser(User):

    college = models.ForeignKey(
        'universities.University',
        on_delete=models.SET_NULL,
        null=True
    )

    college_registry = models.CharField(
        max_length=20
    )

    birthday = models.DateField()
