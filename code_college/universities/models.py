from django.db import models


class University(models.Model):

    users = models.ManyToManyField('users.OrdinaryUser')

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Discipline(models.Model):

    university = models.ForeignKey(
        'University',
        on_delete=models.CASCADE
    )

    projects = models.ManyToManyField('projects.Project')

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
