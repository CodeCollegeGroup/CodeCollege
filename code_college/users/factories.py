import factory
import factory.fuzzy
import datetime
from . import models
from universities.factories import UniversityFactory


class OrdinaryUserFactory(factory.DjangoModelFactory):

    class Meta:
        model = models.OrdinaryUser

    username = factory.Faker('first_name')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.LazyAttribute(lambda o: '%s@example.org' % o.first_name)
    college_registry = factory.Sequence(lambda n: '14/00000%03d' % n)
    birthday = factory.fuzzy.FuzzyDate(datetime.date(1995, 8, 17))
    university = factory.SubFactory(UniversityFactory)

