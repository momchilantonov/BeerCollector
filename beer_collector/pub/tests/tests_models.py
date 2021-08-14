from beer_collector.core.tests.tests_core import CoreTestCase
from PIL import Image


class TestPubModel(CoreTestCase):
    def test_model_fields_type(self):
        self.assertIsInstance(self.pub.name, str)
        self.assertIsInstance(self.pub.address, str)
        self.assertIsInstance(self.pub.description, str)
        self.assertIsInstance(self.pub.website, str)
        self.assertTrue(self.pub.image, Image)
        self.assertTrue(self.pub.latitude, float)
        self.assertTrue(self.pub.longitude, float)
        self.assertEqual(self.pub.user, self.user1)

    def test_model_fields_buildIn_validations(self):
        self.assertEqual(self.pub._meta.get_field('name').max_length, 30)
        self.assertEqual(self.pub._meta.get_field('address').max_length, 60)
        self.assertEqual(self.pub._meta.get_field('description').max_length, 300)
        self.assertEqual(self.pub._meta.get_field('image').upload_to, 'pubs')
        self.assertEqual(self.pub._meta.get_field('longitude').max_digits, 9)
        self.assertEqual(self.pub._meta.get_field('longitude').decimal_places, 6)
        self.assertEqual(self.pub._meta.get_field('latitude').max_digits, 9)
        self.assertEqual(self.pub._meta.get_field('latitude').decimal_places, 6)

    def test_model_relations(self):
        self.assertEqual(len(self.pub_likes), self.pub.publike_set.count())
        for like in self.pub_likes:
            self.assertIn(like, self.pub.publike_set.all())
        self.assertEqual(len(self.pub_comments), self.pub.pubcomment_set.count())
        for comment in self.pub_comments:
            self.assertIn(comment, self.pub.pubcomment_set.all())
