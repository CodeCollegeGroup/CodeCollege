from django.db import models
from users.models import OrdinaryUser


class Project(models.Model):

    title = models.CharField(max_length=50)

    description = models.CharField(max_length=200)

    repository = models.CharField(max_length=100)

    deploy = models.CharField(max_length=100)

    colaborator = models.ManyToMany(OrdinaryUser)

    university_class = models.CharField(max_length=150)

    # evaluation -> falta implementar classe

class Image(models.Model):

    image = models.ImageField(null=True)

    project = models.ForeignKey(Project)
