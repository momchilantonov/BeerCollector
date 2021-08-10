from beer_collector.beer.forms.beer_style import BeerStyleCreateForm, BeerStyleEditForm, BeerStyleCommentForm
from beer_collector.core.tests.core import CoreTestCase


class TestBeerStyleCreateForm(CoreTestCase):
    def test_valid_form(self):
        data = {
            'type': 'testType',
            'description': 'testDesc',
        }
        form = BeerStyleCreateForm(data=data)
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_empty_type_field(self):
        data = {
            'type': '',
            'description': 'testDesc',
        }
        form = BeerStyleCreateForm(data=data)
        print(form.errors)
        self.assertEqual(form.errors['type'], ['This field is required.'])
        self.assertFalse(form.is_valid())


class TestBeerStyleEditForm(CoreTestCase):
    def test_valid_form(self):
        data = {
            'type': 'testType',
            'description': 'testDesc',
        }
        form = BeerStyleEditForm(data=data)
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_empty_type_field(self):
        data = {
            'type': '',
            'description': 'testDesc',
        }
        form = BeerStyleEditForm(data=data)
        print(form.errors)
        self.assertEqual(form.errors['type'], ['This field is required.'])
        self.assertFalse(form.is_valid())


class TestBeerStyleCommentForm(CoreTestCase):
    def test_valid_form(self):
        data = {
            'comment': 'testComment',
            'obj_pk': self.beer_style.id,
        }
        form = BeerStyleCommentForm(data=data)
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_empty_objPK_field(self):
        data = {
            'comment': 'testComment',
            'obj_pk': '',
        }
        form = BeerStyleCommentForm(data=data)
        print(form.errors)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['obj_pk'], ['This field is required.'])
