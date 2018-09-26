from django.test import TestCase
from src.models import Users


class UserTestCase(TestCase):
    def setUp(self):
        self.valid_user = Users.objects.create(
            username='avalidusername',
            email='user@test.com',
            address='somewhere on the planet',
            birthday='2000-03-09'
        )

    def test_instance_variable(self):
        self.assertTrue(isinstance(self.valid_user, Users))

    def test_instance_username(self):
        self.assertTrue(self.valid_user.username, self.valid_user.__unicode__())
