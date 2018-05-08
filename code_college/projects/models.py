from django.db import models
from users.models import OrdinaryUser
from comments.models import Comment


class Project(models.Model):

    owner = models.ForeignKey(
        OrdinaryUser,
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=50, null= False)

    description = models.CharField(max_length=200, null= False)

    repository = models.CharField(max_length=100, null= False)

    deploy = models.CharField(max_length=100)

    colaborators = models.ManyToManyField(OrdinaryUser, related_name='contributed_projects')

    def __str__(self):
        return self.title


class ProjectProxy(Project):
    class Meta:
        ordering = ["title"]
        proxy = True

    def comment(self, project_id, user_id, answer_to, messege, image):

        Comment(project_id, user_id, answer_to, messege, image).save()

    def addCategory(self,projectCategory):

        self.categories.add(projectCategory)


class ProjectImage(models.Model):

    project = models.ForeignKey(
        'projects.Project',
        on_delete=models.CASCADE
    )

    image = models.ImageField()

    def __str__(self):
        return self.image


class ProjectCategory(models.Model):

    class Meta:
        abstract = True

    projects = models.ManyToManyField(Project, related_name='catedories')

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

    def getName():
        return "App"

    def getDescription():
        return "..."


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

    def getName():
        return "Game"

    def getDescription():
        return "..."

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

    def getName():
        return "Web"

    def getDescription():
        return "..."
