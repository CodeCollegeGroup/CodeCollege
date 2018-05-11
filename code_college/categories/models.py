from django.db import models


class ProjectCategory(models.Model):

    projects = models.ManyToManyField('projects.Project')

    name = models.CharField(max_length=200)
    
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class App(ProjectCategory):

    def save(self, args, **kwargs):
        self.pk = 1
        super(App, self).save(args, kwargs)

    def delete(self, *args, kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    class Meta:
        abstract = True


class Game(ProjectCategory):

    def save(self, args, **kwargs):
        self.pk = 1
        super(Game, self).save(args, kwargs)

    def delete(self, *args, kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    class Meta:
        abstract = True


class Web(ProjectCategory):

    def save(self, args, **kwargs):
        self.pk = 1
        super(Web, self).save(args, kwargs)

    def delete(self, *args, kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    class Meta:
        abstract = True


class DenouncementCategory(models.Model):

    denounces = models.ManyToManyField('comments.Denouncement')

    name = models.CharField(max_length=200)

    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Spam(DenouncementCategory):

    def save(self, args, **kwargs):
        self.pk = 1
        super(Web, self).save(args, kwargs)

    def delete(self, *args, kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    class Meta:
        abstract = True


class InappropriateContent(DenouncementCategory):

    def save(self, args, **kwargs):
        self.pk = 1
        super(Web, self).save(args, kwargs)

    def delete(self, *args, kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    class Meta:
        abstract = True


class Piracy(DenouncementCategory):

    def save(self, args, **kwargs):
        self.pk = 1
        super(Web, self).save(args, kwargs)

    def delete(self, *args, kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    class Meta:
        abstract = True
