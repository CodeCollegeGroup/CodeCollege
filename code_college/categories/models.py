from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=200)

    description = models.CharField(max_length=500)

    def delete(self, *args, kwargs):  # pylint: disable=arguments-differ
        pass

    @classmethod
    def load(cls):
        obj, unused_created = cls.objects.get_or_create(pk=1)
        return obj

    def __str__(self):
        return self.name

    def save(self, args, **unused_kwargs):  # pylint: disable=arguments-differ
        self.pk = 1
        super(Category, self).save(args, unused_kwargs)

    class Meta:
        abstract = True


class ProjectCategory(models.Model):

    projects = models.ManyToManyField('projects.Project')


class DenouncementCategory(models.Model):

    denounces = models.ManyToManyField('comments.Denouncement')
