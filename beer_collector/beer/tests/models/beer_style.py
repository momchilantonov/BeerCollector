from beer_collector.core.tests.core import CoreTestCase


class TestBeerStyleModel(CoreTestCase):
    def test_model_fields_type(self):
        self.assertIsInstance(self.beer_style.type, str)
        self.assertIsInstance(self.beer_style.description, str)
        self.assertEqual(self.beer_style.user, self.user1)

    def test_model_fields_buildIn_validations(self):
        self.assertEqual(self.beer_style._meta.get_field('type').max_length, 30)
        self.assertEqual(self.beer_style._meta.get_field('description').max_length, 300)

    def test_model_relations(self):
        self.assertEqual(len(self.beer_style_likes), self.beer_style.beerstylelike_set.count())
        for like in self.beer_style_likes:
            self.assertIn(like, self.beer_style.beerstylelike_set.all())
        self.assertEqual(len(self.beer_style_comments), self.beer_style.beerstylecomment_set.count())
        for comment in self.beer_style_comments:
            self.assertIn(comment, self.beer_style.beerstylecomment_set.all())
