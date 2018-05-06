import factory
from . import models


class UniversityFactory(factory.DjangoModelFactory):

    class Meta:
        model = models.University

    name = factory.Faker('city')


class DisciplineFactory(factory.DjangoModelFactory):

    class Meta:
        model = models.Discipline

    name = factory.Faker('word')
    university = factory.SubFactory(UniversityFactory)
