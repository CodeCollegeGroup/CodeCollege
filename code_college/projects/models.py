from django.db import models


class Project(models.Model):

    recorder = models.ForeignKey(
        'users.OrdinaryUser',
        on_delete=models.CASCADE,
        related_name='created_projects'
    )

    discipline = models.ForeignKey(
        'universities.Discipline',
        on_delete=models.SET_NULL,
        null=True
    )

    contributors = models.ManyToManyField(
        'users.OrdinaryUser',
        related_name='contributed_projects'
    )

    categories = models.ManyToManyField('categories.ProjectCategory')

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
        return self.image
