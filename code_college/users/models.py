from django.db import models
from django.contrib.auth.models import User
from universities.models import University


class OrdinaryUser(User, models.Model):

    birthday = models.DateField()

    college = models.CharField(max_length=80)

    college_registry = models.CharField(max_length=20)

    project = models.ForeignKey(University,
                                on_delete=models.CASCADE,
                                null=True)
