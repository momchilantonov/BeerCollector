from beer_collector.core.tests.core import CoreTestCase
from django.contrib import auth
from django.urls import reverse


class TestIndex(CoreTestCase):
    def test_homePage_withoutProfile(self):
        user = auth.get_user(self.client)
        response = self.client.get(reverse('home page'))
        self.assertTrue(not user.is_authenticated)
        self.assertEqual(response.status_code, 200)

    def test_homePage_withProfile(self):
        self.client.force_login(self.user1)
        user = auth.get_user(self.client)
        response = self.client.get(reverse('home page'))
        self.assertTrue(user.is_authenticated)
        self.assertEqual(response.status_code, 200)
