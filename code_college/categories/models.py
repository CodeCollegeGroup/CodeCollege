from django.db import models

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

