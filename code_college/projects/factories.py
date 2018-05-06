import factory
import factory.fuzzy
import datetime
from . import models
from users.factories import OrdinaryUserFactory
from universities.factories import DisciplineFactory


class ProjectFactory(factory.DjangoModelFactory):

    class Meta:
        model = models.Project

    title = factory.Faker('word')
    description = factory.Faker('word')
    repository = factory.LazyAttribute(lambda o: '%s@github.com' % o.title)
    deploy = factory.LazyAttribute(lambda o: '%s@heroku.com' % o.title)
    discipline = factory.SubFactory(DisciplineFactory)
    recorder = factory.SubFactory(OrdinaryUserFactory)

    @factory.post_generation
    def contributors(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for contributor in extracted:
                self.contributors.add(contributor)


class ProjectImageFactory(factory.DjangoModelFactory):

    class Meta:
        model = models.ProjectImage

    image = factory.django.ImageField(color='pink')
    project = factory.SubFactory(ProjectFactory)
