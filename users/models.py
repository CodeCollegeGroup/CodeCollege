from django.db import models
from django.contrib.auth.models import User

class OrdinaryUser(User, models.Model):

    first_name = models.CharField(blank=False)

    birthday = models.DateField()

    college = models.CharField()

    college_registry = models.CharField()
