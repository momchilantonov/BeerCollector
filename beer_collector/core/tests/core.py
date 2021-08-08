from django.contrib.auth import get_user_model
from django.test import TestCase, Client

UserModel = get_user_model()


class CoreTestCase(TestCase):
    def setUp(self):
        user_email = 'test@test.com'
        user_password = 'test1234'
        self.client = Client()
        self.user = UserModel.objects.create_user(email=user_email, password=user_password)
        self.user.is_active = True
