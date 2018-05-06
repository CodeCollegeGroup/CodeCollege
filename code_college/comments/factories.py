import factory
from . import models
from users.factories import OrdinaryUserFactory
from projects.factories import ProjectFactory


class CommentFactory(factory.DjangoModelFactory):

    class Meta:
        model = models.Comment

    author = factory.SubFactory(OrdinaryUserFactory)
    project = factory.SubFactory(ProjectFactory)
    message = factory.Faker('word')
    image = factory.django.ImageField(color='pink')


class ProjectDenouncementFactory(factory.DjangoModelFactory):

    class Meta:
        model = models.ProjectDenouncement

    message = factory.Faker('word')
    status = 'OP'
    project = factory.SubFactory(ProjectFactory)

    @factory.post_generation
    def categories(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for category in extracted:
                self.categories.add(category)


class CommentDenouncementFactory(factory.DjangoModelFactory):

    class Meta:
        model = models.CommentDenouncement

    message = factory.Faker('word')
    status = 'OP'
    comment = factory.SubFactory(CommentFactory)

    @factory.post_generation
    def categories(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for category in extracted:
                self.categories.add(category)
