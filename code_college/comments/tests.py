from django.test import TestCase
from comments.models import Denouncement, NullState


class TestDenouncement(TestCase):

    def setUp(self):
        self.denouncement = Denouncement(justification="reporting this user")
        self.null_state = NullState.objects.create()

    def test_set_state(self):
        self.denouncement.save()
        self.denouncement.set_state(self.null_state)

        self.assertTrue(
            isinstance(self.denouncement.current_state, NullState)
        )

    def test_save(self):
        self.denouncement.save()

        self.assertTrue(
            isinstance(self.denouncement.current_state,
                       self.denouncement._default_state)
        )

    def test_delete(self):
        self.denouncement.save()
        self.denouncement.set_state(self.null_state)

        with self.assertRaisesMessage(Exception, 'Specific deletion'):
            self.denouncement.delete()

    def test_notify_denouncer(self):
        self.denouncement.save()
        self.denouncement.set_state(self.null_state)

        with self.assertRaisesMessage(Exception, 'Specific notifier'):
            self.denouncement.notify_denouncer()
