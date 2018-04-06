from django.db import models
from django.contrib.auth.models import User

class OrdinaryUser(User, models.Model):

    first_name = models.CharField(blank=False)

    birthday = models.DateField()

    college = models.CharField()

    college_registry = models.CharField()

    def save(self, *args, **kwargs): # pylint: disable=arguments-differ
        super(OrdinaryUser, self).save(*args, **kwargs)
