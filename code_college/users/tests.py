from json import dumps
from django.test import TestCase, Client as ClientTest
from universities.models import University
from .models import OrdinaryUser


class OrdinaryUserTest(TestCase):

    def setUp(self):
        self.user = OrdinaryUser.objects.create_user(
            username='test_user',
            password='test123',
            first_name='Test User',
            birthday='2000-04-04',
            email='test@mail.com',
            college_registry='10/0000000'
        )
        self.university = University(name='UnB', id=1)
        self.client_test = ClientTest()

    def get_json_user(self, obj):
        user = {
            'userid': self.user.id,
            'password': 'test123',
            'new_password': 'TEST123'
        }
        user.update(obj)
        return user

    def test_user_change_password(self):
        user_informations = {
            'new_password_confirmation': 'TEST123'
        }
        response = self.client_test.post('/api/users/password/',
                                         self.get_json_user(
                                            user_informations
                                         ))
        self.assertEqual(response.data, dumps({'detail': 'password changed'}))

    def test_user_change_password_with_different_password(self):
        informations = self.get_json_user({
            'new_password_confirmation': 'test123'
        })
        response = self.client_test.post('/api/users/password/', informations)
        self.assertEqual(
            response.data,
            dumps({'detail': 'different password'})
        )

    def test_user_change_password_with_invalid_password(self):
        user_with_invalid_password = self.get_json_user({
            'password': 'exemplo',
            'new_password_confirmation': 'TEST123'
        })
        response = self.client_test.post(
            '/api/users/password/',
            user_with_invalid_password
        )
        self.assertEqual(response.data, dumps({'detail': 'invalid password'}))

    def test_user_match_change_password(self):
        self.client_test.post('/api/users/password/',
                              {'userid': self.user.pk,
                               'password': 'test123',
                               'new_password': 'DEFAULT123',
                               'new_password_confirmation': 'DEFAULT123',
                               })
        user = OrdinaryUser.objects.get(pk=self.user.pk)
        self.assertTrue(user.check_password('DEFAULT123'))

    def test_get_user(self):
        email = {'email': 'test@mail.com'}
        response = self.client_test.get('/api/users/password/', email)
        self.assertEqual(response.data, dumps({'detail': 'email sent'}))

    def test_get_user_not_found(self):
        response = self.client_test.get('/api/users/password/',
                                        {'email': 'example@mail.com'})
        self.assertEqual(response.data, dumps({'detail': 'user not found'}))
