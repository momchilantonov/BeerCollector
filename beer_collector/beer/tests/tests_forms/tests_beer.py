import tempfile
from beer_collector.beer.forms.beer import BeerCreateForm, BeerEditForm, BeerCommentForm
from beer_collector.core.tests.tests_core import CoreTestCase


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


class TestBeerEditForm(CoreTestCase):
    def test_valid_form(self):
        image1 = tempfile.NamedTemporaryFile(suffix="_test.jpg").name,
        data1 = {
            'label': 'testLabel1',
            'type': self.beer_style,
            'description': 'testDesc1',
        }
        files1 = {
            'file': image1,
        }
        create_form = BeerCreateForm(data=data1, files=files1)
        print(create_form.errors)
        self.assertTrue(create_form.is_valid)

        image2 = tempfile.NamedTemporaryFile(suffix="_test.jpg").name,
        data2 = {
            'label': 'testLabel2',
            'type': self.beer_style,
            'description': 'testDesc2',
        }
        files2 = {
            'file': image2,
        }
        edit_form = BeerEditForm(data=data2, files=files2)
        print(edit_form.errors)
        self.assertEqual(create_form.data['label'], 'testLabel1')
        self.assertEqual(edit_form.data['label'], 'testLabel2')
        self.assertNotEqual(create_form.data['label'], edit_form.data['label'])
        self.assertEqual(create_form.data['type'], self.beer_style)
        self.assertEqual(edit_form.data['type'], self.beer_style)
        self.assertEqual(create_form.data['type'], edit_form.data['type'])
        self.assertEqual(create_form.data['description'], 'testDesc1')
        self.assertEqual(edit_form.data['description'], 'testDesc2')
        self.assertNotEqual(create_form.data['description'], edit_form.data['description'])
        self.assertEqual(create_form.files['file'], image1)
        self.assertEqual(edit_form.files['file'], image2)
        self.assertNotEqual(create_form.files['file'], edit_form.files['file'])
        self.assertTrue(edit_form.is_valid)


class TestBeerCommentForm(CoreTestCase):
    def test_valid_form(self):
        data = {
            'comment': 'testComment',
            'obj_pk': self.beer.id,
        }
        form = BeerCommentForm(data=data)
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_empty_objPK_field(self):
        data = {
            'comment': 'testComment',
            'obj_pk': '',
        }
        form = BeerCommentForm(data=data)
        print(form.errors)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['obj_pk'], ['This field is required.'])
