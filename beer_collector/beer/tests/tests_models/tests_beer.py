from beer_collector.core.tests.tests_core import CoreTestCase
from PIL import Image


class TestBeerModel(CoreTestCase):
    def test_model_fields_type(self):
        self.assertIsInstance(self.beer.label, str)
        self.assertEqual(self.beer.type, self.beer_style)
        self.assertIsInstance(self.beer.description, str)
        self.assertTrue(self.beer.image, Image)
        self.assertEqual(self.beer.user, self.user1)

    def test_model_fields_buildIn_validations(self):
        self.assertEqual(self.beer._meta.get_field('label').max_length, 30)
        self.assertEqual(self.beer._meta.get_field('description').max_length, 300)
        self.assertEqual(self.beer._meta.get_field('image').upload_to, 'beers')

    def test_model_relations(self):
        self.assertEqual(len(self.beer_likes), self.beer.beerlike_set.count())
        for like in self.beer_likes:
            self.assertIn(like, self.beer.beerlike_set.all())
        self.assertEqual(len(self.beer_comments), self.beer.beercomment_set.count())
        for comment in self.beer_comments:
            self.assertIn(comment, self.beer.beercomment_set.all())
