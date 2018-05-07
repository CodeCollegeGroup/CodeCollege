from datetime import datetime
from django.test import TestCase
from users.models import OrdinaryUser
from projects.models import Project
from .models import Denouncement, NullState, Comment, Rating


class TestFeedbacksFeature(TestCase):

    def setUp(self):
        self.user = OrdinaryUser.objects.create_user(
            username='username',
            password='passoword',
            birthday=datetime(2018, 1, 1),
            college_registry='11/111111111'
        )

        self.project = Project.objects.create(
            owner=self.user,
            title='title',
            description='description',
            repository='repository',
            deploy='deploy'
        )

        self.denouncement = Denouncement(
            project=self.project,
            author=self.user,
            date_time=datetime(2018, 1, 1, 1, 1, 1),
            justification='justification'
        )

        self.comment = Comment.objects.create(
            project=self.project,
            author=self.user,
            date_time=datetime(2018, 1, 1, 1, 1, 1)
        )

        self.rating = Rating.objects.create(
            project=self.project,
            author=self.user,
            date_time=datetime(2018, 1, 1, 1, 1, 1),
            like=True,
        )

        self.null_state = NullState.objects.create()

    def test_save_comment(self):
        self.comment.save()

    def test_save_rating(self):
        self.rating.save()

    def test_create_denouncement(self):
        self.denouncement.save()

    def test_set_state(self):
        self.denouncement.save()
        self.denouncement.set_state(self.null_state)

        self.assertTrue(
            isinstance(self.denouncement.current_state, NullState)
        )

    def test_save(self):
        self.denouncement.save()

        # pylint: disable=protected-access
        self.assertTrue(
            isinstance(self.denouncement.current_state,
                       self.denouncement._default_state)
        )
        # pylint: disable=protected-access

    def test_delete(self):
        self.denouncement.save()
        self.denouncement.set_state(self.null_state)

        with self.assertRaisesMessage(Exception, 'Specific deletion'):
            self.denouncement.delete_denouncement()

    def test_notify_denouncer(self):
        self.denouncement.save()
        self.denouncement.set_state(self.null_state)

        with self.assertRaisesMessage(Exception, 'Specific notifier'):
            self.denouncement.notify_denouncer()
