from django.db import models


class University(models.Model):

    users = models.ManyToManyField(
        'users.OrdinaryUser',
        related_name='students'
    )

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Discipline(models.Model):

    university = models.ForeignKey(
        'University',
        related_name='univerisities',
        on_delete=models.CASCADE
    )

    projects = models.ManyToManyField('projects.Project')

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
