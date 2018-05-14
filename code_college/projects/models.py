from django.db import models
from users.models import OrdinaryUser


class Project(models.Model):

    owner = models.ForeignKey(
        'users.OrdinaryUser',
        on_delete=models.CASCADE,
        related_name='owner_projects'
    )

    contributors = models.ManyToManyField(
        OrdinaryUser,
        related_name='contributed_projects'
    )

    title = models.CharField(
        max_length=200
    )

    description = models.CharField(
        max_length=500
    )

    repository = models.CharField(
        max_length=300
    )

    deploy = models.CharField(
        max_length=300
    )

    def __str__(self):
        return self.title


class ProjectImage(models.Model):

    project = models.ForeignKey(
        'projects.Project',
        on_delete=models.CASCADE
    )

    image = models.ImageField()

    def __str__(self):
        return self.image.url
