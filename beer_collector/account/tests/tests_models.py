from datetime import datetime
from beer_collector.core.tests.tests_core import CoreTestCase


class TestAccountModel(CoreTestCase):
    def test_model_fields_type(self):
        self.assertIsInstance(self.user1.email, str)
        self.assertIsInstance(self.user1.date_joined, datetime)
        self.assertIsInstance(self.user1.last_login, datetime)
        self.assertIsInstance(self.user1.is_active, bool)
        self.assertIsInstance(self.user1.is_staff, bool)
        self.assertIsInstance(self.user1.is_superuser, bool)

    def test_model_fields_buildIn_validations(self):
        self.assertTrue(self.user1._meta.get_field('email').unique)
        self.assertTrue(self.user1._meta.get_field('date_joined').auto_now_add)
        self.assertTrue(self.user1._meta.get_field('last_login').auto_now)
        self.assertTrue(self.user1._meta.get_field('is_active').default)
        self.assertFalse(self.user1._meta.get_field('is_staff').default)
        self.assertFalse(self.user1._meta.get_field('is_superuser').default)
