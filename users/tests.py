from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import (
    BACKEND_SESSION_KEY, SESSION_KEY, _clean_credentials, authenticate,
    get_user, signals,
)

class LoginTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='client', password='admin')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        user = authenticate(username='client', password='admin')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='wrong', password='admin')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_password(self):
        user = authenticate(username='client', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)
