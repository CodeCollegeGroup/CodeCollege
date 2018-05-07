from django.db import models


class FeedbackFeature(models.Model):

    project = models.ForeignKey(
        'projects.Project',
        on_delete=models.CASCADE
    )

    author = models.ForeignKey(
        'users.OrdinaryUser',
        on_delete=models.CASCADE
    )

    date_time = models.DateTimeField()


class Comment(FeedbackFeature):

    feed_back = models.ManyToManyField(
        'FeedbackFeature',
        related_name='comments'
    )

    message = models.CharField(max_length=400)

    def answer(self):
        pass

    def dennounce(self):
        pass

    def like(self):
        pass

    def delete(self):
        pass

    def change(self):
        pass

    def __str__(self):
        return self.message


class Rating(FeedbackFeature):

    like = models.BooleanField()

    def change(self):
        pass

    def __str__(self):
        return self.like


class Denouncement(FeedbackFeature):

    justification = models.CharField(max_length=500)

    solved = models.BooleanField()

    def __str__(self):
        return self.justification
