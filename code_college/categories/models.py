from django.db import models


class ProjectCategory(models.Model):

    projects = models.ManyToManyField('projects.Project')

    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class App(ProjectCategory):

    def delete(self, *args, kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    def getName():
        return "App"

    def getDescription():
        return "..."

    def save(self, args, **kwargs):
        self.pk = 1
        super(App, self).save(args, kwargs)

    class Meta:
        abstract = True


class Game(ProjectCategory):

    def delete(self, *args, kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    def getName():
        return "Game"

    def getDescription():
        return "..."

    def save(self, args, **kwargs):
        self.pk = 1
        super(Game, self).save(args, kwargs)

    class Meta:
        abstract = True


class Web(ProjectCategory):

    def delete(self, *args, kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    def getName():
        return "Web"

    def getDescription():
        return "..."

    def save(self, args, **kwargs):
        self.pk = 1
        super(Web, self).save(args, kwargs)

    class Meta:
        abstract = True


class DenouncementCategory(models.Model):

    denounces = models.ManyToManyField('comments.Denouncement')

    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
