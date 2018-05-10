import factory
from . import models


class UniversityFactory(factory.DjangoModelFactory):

    class Meta:
        model = models.University

    name = factory.Faker(
        'city'
    )


class DisciplineFactory(factory.DjangoModelFactory):

    class Meta:
        model = models.Discipline

    university = factory.SubFactory(
        UniversityFactory
    )

    name = factory.Faker(
        'word'
    )
