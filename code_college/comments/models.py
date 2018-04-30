from django.db import models


class Comment(models.Model):

    project = models.ForeignKey(
        'projects.Project',
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

    message = models.CharField(max_length=400)

    image = models.ImageField()

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

    category = models.ForeignKey(
        'categories.DenouncementCategory',
        on_delete=models.CASCADE
    )

    message = models.CharField(max_length=500)

    status = models.CharField(
        max_length=12,
        choices=STATUS,
        default=OPEN
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.message


class ProjectDenouncement(Denouncement):

    project = models.ForeignKey(
        'projects.Project',
        on_delete=models.CASCADE
    )


class CommentDenouncement(Denouncement):

    comment = models.ForeignKey(
        'Comment',
        on_delete=models.CASCADE
    )


class Rating(models.Model):

    appraiser = models.ForeignKey(
        'users.OrdinaryUser',
        on_delete=models.CASCADE
    )

    like = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.like


class ProjectRating(Rating):

    project = models.ForeignKey(
        'projects.Project',
        on_delete=models.CASCADE
    )


class CommentRating(Rating):

    comment = models.ForeignKey(
        'Comment',
        on_delete=models.CASCADE
    )
