from django.db import models
from django.contrib.auth.models import User


class OrdinaryUser(User, models.Model):

    birthday = models.DateField()

    college_registry = models.CharField(max_length=20)
