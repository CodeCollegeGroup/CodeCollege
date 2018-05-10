import factory
from . import models


class ProjectCategoryFactory(factory.DjangoModelFactory):

    class Meta:
        model = models.ProjectCategory

    name = factory.Faker(
        'word'
    )

    description = factory.Faker(
        'word'
    )

    @factory.post_generation
    def projects(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for project in extracted:
                self.projects.add(project)


class DenouncementCategoryFactory(factory.DjangoModelFactory):

    class Meta:
        model = models.DenouncementCategory

    name = factory.Faker(
        'word'
    )

    description = factory.Faker(
        'word'
    )

    @factory.post_generation
    def denounces(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for denouncement in extracted:
                self.denounces.add(denouncement)
