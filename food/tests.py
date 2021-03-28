from django.test import RequestFactory, TestCase
from http import HTTPStatus
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.messages import get_messages
from django.contrib.messages.storage.fallback import FallbackStorage
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.messages.middleware import MessageMiddleware

from .models import Food
from .views import all_foods, edit_foods, one_food
from .forms import FoodForm

class FoodModelTest(TestCase):
    def setUp(self):
        self.food = Food.objects.create()
        self.food.save()

    def tearDown(self):
        self.food.delete()

    def test_create(self):
        self.assertEqual(self.food.id, 1)

class FoodFormTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        # Create dummy food
        self.food = Food.objects.create()
        # Create dummy user
        self.user = User.objects.create_user(username='client', password='admin')
        # Add group to user
        self.user.groups.add(Group.objects.get(name='Client'))
        self.user.save()    

        self.food = Food.objects.create()
        self.food.user = self.user
        self.food.save()

    def tearDown(self):
        self.user.delete()
        self.food.delete()

    def test_allFood(self):
        request = self.factory.get("/food")

        # User without permission
        request.user = User.objects.create_user(username='test', password='test')
        response = all_foods(request)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

        request.user = self.user
        response = all_foods(request)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_editFood(self):
        request = self.factory.get("/food/editFood" + str())

        # User without permission
        request.user = User.objects.create_user(username='test', password='test')
        # Set session and messages attribute
        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)
        response = edit_foods(request, self.food.id)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

        request = self.factory.get("/food/editFood")
        request.user = self.user
        # Set session and messages attribute
        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)
        response = edit_foods(request, self.food.id)
        self.assertEqual(response.status_code, HTTPStatus.OK)


        request = self.factory.post("/food/editFood", { 'name': "Test name"})
        request.user = self.user
        # Set session and messages attribute
        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)
        response = edit_foods(request, self.food.id)
        self.assertEqual(response.status_code, HTTPStatus.OK)