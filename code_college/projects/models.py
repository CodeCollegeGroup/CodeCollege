from django.db import models
from universities.models import Discipline
from categories.models import ProjectCategory
from users.models import User


class Project(models.Model):

    title = models.CharField(max_length=200)

    description = models.CharField(max_length=500)

    repository = models.CharField(max_length=300)

    deploy = models.CharField(max_length=300)

    discipline = models.ForeignKey(Discipline,
                                   on_delete=models.DO_NOTHING,
                                   null=True)

    # Como validar ao menos 1?
    contributors = models.ManyToManyField(User)

    categories = models.ManyToManyField(ProjectCategory)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):

    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    image = models.ImageField

    def __str__(self):
        return self.image.name
