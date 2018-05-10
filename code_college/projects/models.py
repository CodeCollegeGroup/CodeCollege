from django.db import models
from users.models import OrdinaryUser
from comments.models import Comment


class Project(models.Model):

    owner = models.ForeignKey(
        'users.OrdinaryUser',
        on_delete=models.CASCADE,
        related_name='owner_projects'
    )

    contributors = models.ManyToManyField(
        OrdinaryUser,
        related_name='contributed_projects'
    )

    title = models.CharField(
        max_length=200
    )

    description = models.CharField(
        max_length=500
    )

    repository = models.CharField(
        max_length=300
    )

    deploy = models.CharField(
        max_length=300
    )

    #  categoties ...

    def __str__(self):
        return self.title


class ProjectProxy(Project):

    def comment(self, user_id, components, message):
        base = CommentBase()
        base.text = messege
        base.author = OrdinaryUser.objects.get(id=user_id)
        base.project = self

        for aux in range(len(components)-1):
            components[aux].decorator = components[aux+1]

        components[len(components)-1].decorator = base
        components[len(components)-1].save()    


    def addCategory(self,projectCategory):
        self.categories.add(projectCategory)

    class Meta:
        ordering = ["title"]
        proxy = True


class ProjectImage(models.Model):

    project = models.ForeignKey(
        'projects.Project',
        on_delete=models.CASCADE
    )

    image = models.ImageField()

    def __str__(self):
        return self.image.url


class ProjectCategory(models.Model):

    projects = models.ManyToManyField(
        Project, related_name='categories'
    )

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class App(ProjectCategory):

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    def getName():
        return "App"

    def getDescription():
        return "..."

    def delete(self, *args, **kwargs):
        pass

    def save(self, *args, **kwargs):
        self.pk = 1
        super(App, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class Game(ProjectCategory):

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    def getName():
        return "Game"

    def getDescription():
        return "..."

    def save(self, *args, **kwargs):
        self.pk = 1
        super(Game, self).save(*args, **kwargs)

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        pass


class Web(ProjectCategory):

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    def getName():
        return "Web"

    def getDescription():
        return "..."

    def save(self, *args, **kwargs):
        self.pk = 1
        super(Web, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    class Meta:
        abstract = True
