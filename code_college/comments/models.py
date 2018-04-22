from django.db import models
from users.models import User
from projects.models import Project
from categories.models import DenouncementCategory

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


class Rating(models.Model):
    like = models.BooleanField(default=True)
    appraiser = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def __str__(self):
        return self.like


class ProjectRating(Rating):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class CommentRating(Rating):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
