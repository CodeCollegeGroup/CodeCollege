from django.db import models
from django.contrib.auth.models import User
from comments.migrations import Rating

class OrdinaryUser(User):

    university = models.ForeignKey(
        'universities.University',
        related_name='students',
        on_delete=models.SET_NULL,
        null=True
    )

    college_registry = models.CharField(
        max_length=20
    )

    birthday = models.DateField()
    college_registry = models.CharField(max_length=20)

<<<<<<< HEAD

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

    def search(self, user_id):
        user = User.objects.get(user_id)
        result = self.get_result(user)
        return result

    def get_result(self, user):
        pass


class ProjectOwner(Profile):

    def get_result(self, user):
        return user.created_projects.all()


class ProjectContributes(Profile):

    def get_result(self, user):
        return user.contributed_projects.all()


class CommentsOwner(Profile):

    def get_result(self, user):
        return user.author_comments.all()
=======
class Profile(models.Model):
    pass
>>>>>>> Add Profile class
