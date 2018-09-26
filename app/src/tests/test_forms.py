from django.test import TestCase
from src.forms import RegisterForm


class TestRegistrationForm(TestCase):

    def test_registration_form_invalid(self):
        # test invalid data
        invalid_data = {
            "username": "ausernamewhichislongerthan30charecter",
            "email": "user@test.com",
            "address": "somewhere on the planet",
            "birthday": "2000-03-09"
        }
        form = RegisterForm(data=invalid_data)
        form.is_valid()
        self.assertTrue(form.errors)

    def test_registration_form_valid(self):
        # test valid data
        valid_data = {
            "username": "avalidusername",
            "email": "user@test.com",
            "address": "somewhere on the planet",
            "birthday": "2000-03-09"
        }
        form = RegisterForm(data=valid_data)
        form.is_valid()
        self.assertFalse(form.errors)
