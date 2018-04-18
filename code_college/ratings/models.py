from django.db import models
from users.models import User
from projects.models import Project
from projects.models import Comment


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
