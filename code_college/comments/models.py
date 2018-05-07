from django.db import models


class FeedbackFeature:

    project = models.ForeignKey(
        'projects.Project',
        on_delete=models.CASCADE
    )

    author = models.ForeignKey(
        'users.OrdinaryUser',
        on_delete=models.CASCADE
    )

    date_time = models.DateTimeField()

    class Meta:
        abstract = True


class Comment(FeedbackFeature):

    feed_back = models.ManyToManyField('FeedbackFeature')

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

    class Meta:
        abstract = True

    def __str__(self):
        return self.justification
