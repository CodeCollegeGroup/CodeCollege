from django.db import models
from users.models import OrdinaryUser
from comments.models import Comment


class Project(models.Model):

    owner = models.ForeignKey(
        OrdinaryUser,
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=50, null=False)

    description = models.CharField(max_length=200, null=False)

    repository = models.CharField(max_length=100, null=False)

    deploy = models.CharField(max_length=100)

    colaborators = models.ManyToManyField(
            OrdinaryUser,
            related_name='contributed_projects'
    )

    #  categoties ...

    def __str__(self):
        return self.title


class ProjectProxy(Project):
    class Meta:
        ordering = ["title"]
        proxy = True

    def comment(self, user_id, components, message):

        base = CommentBase()
        base.text = messege
        base.author = OrdinaryUser.objects.get(id=user_id)
        base.project = self

        for aux in range(len(components)-1):
            components[aux].decorator = components[aux+1]

        components[len(components)-1].decorator = base
        components[len(components)-1].save()    




class ProjectImage(models.Model):

    project = models.ForeignKey(
        'projects.Project',
        on_delete=models.CASCADE
    )

    image = models.ImageField()

    def __str__(self):
        return self.image
