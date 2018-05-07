from django.db import models
from users.models import OrdinaryUser

class ProjectCategory(models.Model):

    description = models.CharField(max_length=500)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class App(ProjectCategory):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(App, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

class Game(ProjectCategory):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(Game, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

class Web(ProjectCategory):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(Web, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class Project(models.Model):

    recorder = models.ForeignKey(OrdinaryUser, on_delete=models.CASCADE)

    title = models.CharField(max_length=50, null= False)

    description = models.CharField(max_length=200, null= False)

    repository = models.CharField(max_length=100, null= False)

    deploy = models.CharField(max_length=100)

    colaborators = models.ManyToManyField(OrdinaryUser, related_name='contributed_projects')

    category = models.CharField(max_length=10)


    # university_class =


class ProjectProxy(Project):
    class Meta:
        ordering = ["title"]
        proxy = True

    def comment(self, project_id, user_id, answer_to, messege, image):

            Comment(project_id, user_id, answer_to, messege, image).save()





class Image(models.Model):

    # image = models.ImageField(null=True)

    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class Comment(models.Model):

    project = models.ForeignKey(
        'project.Project',
        on_delete=models.CASCADE
    )

    author = models.ForeignKey(
        'users.OrdinaryUser',
        on_delete=models.CASCADE
    )

    answer_to = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True
    )

    message = models.CharField(max_length=500)

    # image = models.ImageField()

    def __str__(self):
        return self.message
