from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from src.models import Users


class TestUserRegistrationView(TestCase):
    url = reverse('register')

    def setUp(self):
        self.client = Client()

    def test_register_post_method_should_be_405(self):
        # test req method GET
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 405)

    def test_register_post_empty_data(self):
        # test req method POST with empty data
        response = self.client.post(self.url, {})
        self.assertEqual(response.status_code, 202)
        exp_data = {
            'result': False,
            'message': {
                'email': ['This field is required.'],
                'username': ['This field is required.'],
                'address': ['This field is required.'],
                'birthday': ['This field is required.']
            }
        }
        self.assertEqual(exp_data, response.json())

    def test_register_invalid_data(self):
        # test req method POST with invalid data
        # test invalid data
        invalid_data = {
            "username": "ausernamewhichislongerthan30charecter",
            "email": "user@test.com",
            "address": "somewhere on the planet",
            "birthday": "2000-03-09"
        }
        response = self.client.post(self.url, invalid_data)
        self.assertEqual(response.status_code, 202)
        exp_data = {
            'result': False,
            'message': {
                'username': ['Ensure this value has at most 30 characters (it has 37).']
            }
        }
        self.assertEqual(exp_data, response.json())

    def test_register_valid_data(self):
        # test req method POST with valid data
        # test valid data
        valid_data = {
            "username": "avalidusername",
            "email": "user@test.com",
            "address": "somewhere on the planet",
            "birthday": "2000-03-09"
        }
        response = self.client.post(self.url, valid_data)
        self.assertEqual(response.status_code, 201)
        exp_data = {
            "result": True,
            "message": "User is recorded with given informations."
        }
        self.assertEqual(exp_data, response.json())


class TestUsersView(TestCase):
    url = reverse('users')

    def setUp(self):
        self.client = Client()
        Users.objects.create(
            username = "user-1",
            email = "user-test-1@gmail.com",
            address = "test address",
            birthday = "2000-09-03"
        )
        Users.objects.create(
            username = "user-2",
            email = "user-test-2@gmail.com",
            address = "test address",
            birthday = "2000-09-03"
        )

    def test_user_post_method_should_be_405(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 405)

    def test_get_all_users(self):
        response = self.client.get(self.url)
        self.assertEqual(len(response.json()), 2)


class TestUserView(TestCase):
    url = reverse('user')

    def setUp(self):
        self.client = Client()
        Users.objects.create(
            username = "user-1",
            email = "user-test-1@gmail.com",
            address = "test address",
            birthday = "2000-09-03"
        )
        Users.objects.create(
            username = "user-2",
            email = "user-test-2@gmail.com",
            address = "test address",
            birthday = "2000-09-03"
        )

    def test_user_post_method_should_be_405(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 405)

    def test_get_a_user(self):
        response = self.client.get(self.url, {"username": "user-1"})
        self.assertEqual(len(response.json()), 1)

