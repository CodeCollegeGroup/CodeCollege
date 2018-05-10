from django.db import models


class ProjectCategory(models.Model):

    projects = models.ManyToManyField('projects.Project')
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class App(ProjectCategory):
    class Meta:
        abstract = True

    def save(self, args, **kwargs):
        self.pk = 1
        super(App, self).save(args, kwargs)

    def delete(self, *args, kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class Game(ProjectCategory):
    class Meta:
        abstract = True

    def save(self, args, **kwargs):
        self.pk = 1
        super(Game, self).save(args, kwargs)

    def delete(self, *args, kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class Web(ProjectCategory):
    class Meta:
        abstract = True

    def save(self, args, **kwargs):
        self.pk = 1
        super(Web, self).save(args, kwargs)

    def delete(self, *args, kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class DenouncementCategory(models.Model):

    denounces = models.ManyToManyField('comments.Denouncement')
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class Spam(DenouncementCategory):
    class Meta:
        abstract = True

    def save(self, args, **kwargs):
        self.pk = 1
        super(Web, self).save(args, kwargs)

    def delete(self, *args, kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

class InappropriateContent(DenouncementCategory):
    class Meta:
        abstract = True

    def save(self, args, **kwargs):
        self.pk = 1
        super(Web, self).save(args, kwargs)

    def delete(self, *args, kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

class Piracy(DenouncementCategory):
    class Meta:
        abstract = True

    def save(self, args, **kwargs):
        self.pk = 1
        super(Web, self).save(args, kwargs)

    def delete(self, *args, kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj
