from django.db import models
from universities.models import Discipline
from users.models import User


class Category(models.Model):

    name = models.CharField(max_length=200)

    description = models.CharField(max_length=500)

    class Meta:

        abstract = True

    def __str__(self):
        return self.name


class ProjectCategory(Category):

    pass


class DenouncementCategory(Category):

    pass


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


class Comment(models.Model):

    message = models.CharField(max_length=400)

    image = models.ImageField

    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    answer_to = models.ForeignKey('self', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.message


class Denouncement(models.Model):

    OPEN = 'OP'
    IN_ANALYSIS = 'AL'
    CLOSED = 'CL'

    STATUS = (
        (OPEN, 'open'),
        (IN_ANALYSIS, 'in analysis'),
        (CLOSED, 'closed'),
    )

    message = models.CharField(max_length=500)

    status = models.CharField(max_length=12, choices=STATUS, default=OPEN)

    category = models.ForeignKey(DenouncementCategory,
                                 on_delete=models.CASCADE)

    class Meta:

        abstract = True

    def __str__(self):
        return self.message


class ProjectDenouncement(Denouncement):

    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class CommentDenouncement(Denouncement):

    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
