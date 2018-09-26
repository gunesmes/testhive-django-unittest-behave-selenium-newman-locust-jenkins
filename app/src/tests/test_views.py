from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse


class TestUserRegistrationView(TestCase):
    url = reverse('register')

    def setUp(self):
        self.client = Client()

    def test_register_get_method(self):

        # test req method GET
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

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

