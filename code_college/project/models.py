from django.db import models
from users.models import OrdinaryUser


class Project(models.Model):

    recorder = models.ForeignKey(OrdinaryUser, on_delete=models.CASCADE)

    title = models.CharField(max_length=50, null= False)

    description = models.CharField(max_length=200, null= False)

    repository = models.CharField(max_length=100, null= False)

    deploy = models.CharField(max_length=100)

    colaborator = models.ManyToManyField(OrdinaryUser, related_name='contributed_projects')

    university_class = models.CharField(max_length=150)


class ProjectProxy(Project):
    class Meta:
        ordering = ["title"]
        proxy = True

    def comment(self, project_id, user_id, answer_to, messege, image):

            Comment(project_id, user_id, answer_to, messege, image).save()



class Image(models.Model):

    # image = models.ImageField(null=True)

    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class Comment(models.Model):

    project = models.ForeignKey(
        'project.Project',
        on_delete=models.CASCADE
    )

    author = models.ForeignKey(
        'users.OrdinaryUser',
        on_delete=models.CASCADE
    )

    answer_to = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True
    )

    message = models.CharField(max_length=500)

    # image = models.ImageField()

    def __str__(self):
        return self.message
