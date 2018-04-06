from django.db import models
from django.contrib.auth.models import User

class OrdinaryUser(User, models.Model):

    birthday = models.DateField()

    college = models.CharField(max_length=80)

    college_registry = models.CharField(max_length=20)

    def save(self, *args, **kwargs): # pylint: disable=arguments-differ
        super(OrdinaryUser, self).save(*args, **kwargs)
