import tempfile
from beer_collector.beer.forms.beer import BeerCreateForm
from beer_collector.core.tests.core import CoreTestCase


class TestBeerCreateForm(CoreTestCase):
    def test_valid_form(self):
        data = {
            'label': 'testLabel',
            'type': self.beer_style,
            'description': 'testDesc',
        }
        files = {
            'file': tempfile.NamedTemporaryFile(suffix="_test.jpg").name,
        }
        form = BeerCreateForm(data=data, files=files)
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_empty_type_field(self):
        data = {
            'label': 'testLabel',
            'type': '',
            'description': 'testDesc',
        }
        files = {
            'file': tempfile.NamedTemporaryFile(suffix="_test.jpg").name,
        }
        form = BeerCreateForm(data=data, files=files)
        print(form.errors)
        self.assertEqual(form.errors['type'], ['This field is required.'])
        self.assertFalse(form.is_valid())

    def test_upload_large_image(self):
        data = {
            'label': 'testLabel',
            'type': self.beer_style,
            'description': 'testDesc',
        }
        files = {
            'image': self.large_image_for_test,
        }
        form = BeerCreateForm(data=data, files=files)
        print(form.errors)
        self.assertEqual(form.errors['image'], ['Width or Height is larger than what is allowed.'])
        self.assertFalse(form.is_valid())
