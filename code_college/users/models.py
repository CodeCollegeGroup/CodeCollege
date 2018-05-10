from django.db import models
from django.contrib.auth.models import User


class OrdinaryUser(User, models.Model):

    colaborated_projects = models.ForeignKey(
        'projects.Project',
        on_delete=models.SET_NULL,
        null=True
    )

    birthday = models.DateField()

    college_registry = models.CharField(max_length=20)


class Profile(models.Model):

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(Profile, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    def search_project_owner(self, user_id):
        user = User.objects.get(user_id)
        projects = user.created_projects.all()
        return projects

    def search_project_contributes(self, user_id):
        user = User.objects.get(user_id)
        contributors = user.contributed_projects.all()
        return contributors

    def search_comments_owner(self, user_id):
        user = User.objects.get(user_id)
        comments = user.author_comments.all()
        return comments
