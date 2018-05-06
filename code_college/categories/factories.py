import factory
from . import models


class ProjectCategoryFactory(factory.DjangoModelFactory):

    class Meta:
        model = models.ProjectCategory

    name = factory.Faker('word')
    description = factory.Faker('word')


class DenouncementCategoryFactory(factory.DjangoModelFactory):

    class Meta:
        model = models.DenouncementCategory

    name = factory.Faker('word')
    description = factory.Faker('word')
