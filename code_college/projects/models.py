from django.db import models


class Project(models.Model):

    owner = models.ForeignKey(
        'users.OrdinaryUser',
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=200)

    description = models.CharField(max_length=500)

    repository = models.CharField(max_length=300)

    deploy = models.CharField(max_length=300)

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
