from django.db import models
from django.contrib.auth.models import User


class OrdinaryUser(User):

    university = models.ForeignKey(
        'universities.University',
        related_name='students',
        on_delete=models.SET_NULL,
        null=True
    )

    college = models.ForeignKey(
        'universities.University',
        related_name='universities',
        on_delete=models.SET_NULL,
        null=True
    )

    birthday = models.DateField()

    college_registry = models.CharField(max_length=20)


class Profile(models.Model):

    def delete(self, *args, **kwargs):  # pylint: disable=arguments-differ
        pass

    @classmethod
    def load(cls):
        obj, unused_created = cls.objects.get_or_create(pk=1)
        return obj

    def search(self, user_id):
        user = User.objects.get(user_id)
        result = self.get_result(user)
        return result

    def get_result(self, user):
        pass

    def save(self, *args, **kwargs):  # pylint: disable=arguments-differ
        self.pk = 1
        super(Profile, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class ProjectOwner(Profile):

    def get_result(self, user):
        return user.created_projects.all()


class ProjectContributes(Profile):

    def get_result(self, user):
        return user.contributed_projects.all()


class CommentsOwner(Profile):

    def get_result(self, user):
        return user.author_comments.all()
