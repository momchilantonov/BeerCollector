import tempfile
from beer_collector.beer.forms.beer import BeerCreateForm, BeerEditForm, BeerCommentForm
from beer_collector.core.tests.tests_core import CoreTestCase
from beer_collector.pub.forms import PubCreateForm, PubEditForm, PubCommentForm


class TestPubCreateForm(CoreTestCase):
    def test_valid_form(self):
        data = {
            'name': 'testPub1',
            'address': 'testAddress1',
            'description': 'testDesc1',
            'website': 'https://www.test1.com/',
            'longitude': 23.111111,
            'latitude': 41.000000,
        }
        files = {
            'file': tempfile.NamedTemporaryFile(suffix="_test.jpg").name,
        }
        form = PubCreateForm(data=data, files=files)
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_empty_type_field(self):
        data = {
            'name': '',
            'address': 'testAddress1',
            'description': 'testDesc1',
            'website': 'https://www.test1.com/',
            'longitude': 23.111111,
            'latitude': 41.000000,
        }
        files = {
            'file': tempfile.NamedTemporaryFile(suffix="_test.jpg").name,
        }
        form = PubCreateForm(data=data, files=files)
        print(form.errors)
        self.assertEqual(form.errors['name'], ['This field is required.'])
        self.assertFalse(form.is_valid())

    def test_upload_large_image(self):
        data = {
            'name': 'testPub1',
            'address': 'testAddress1',
            'description': 'testDesc1',
            'website': 'https://www.test1.com/',
            'longitude': 23.111111,
            'latitude': 41.000000,
        }
        files = {
            'image': self.large_image_for_test,
        }
        form = PubCreateForm(data=data, files=files)
        print(form.errors)
        self.assertEqual(form.errors['image'], ['Width or Height is larger than what is allowed.'])
        self.assertFalse(form.is_valid())


class TestPubEditForm(CoreTestCase):
    def test_valid_form(self):
        image1 = tempfile.NamedTemporaryFile(suffix="_test.jpg").name,
        data1 = {
            'name': 'testPub1',
            'address': 'testAddress1',
            'description': 'testDesc1',
        }
        files1 = {
            'file': image1,
        }
        create_form = PubCreateForm(data=data1, files=files1)
        print(create_form.errors)
        self.assertTrue(create_form.is_valid)

        image2 = tempfile.NamedTemporaryFile(suffix="_test.jpg").name,
        data2 = {
            'name': 'testPub2',
            'address': 'testAddress2',
            'description': 'testDesc2',
        }
        files2 = {
            'file': image2,
        }
        edit_form = PubEditForm(data=data2, files=files2)
        print(edit_form.errors)
        self.assertEqual(create_form.data['name'], 'testPub1')
        self.assertEqual(edit_form.data['name'], 'testPub2')
        self.assertNotEqual(create_form.data['name'], edit_form.data['name'])
        self.assertEqual(create_form.data['address'], 'testAddress1')
        self.assertEqual(edit_form.data['address'], 'testAddress2')
        self.assertNotEqual(create_form.data['address'], edit_form.data['address'])
        self.assertEqual(create_form.data['description'], 'testDesc1')
        self.assertEqual(edit_form.data['description'], 'testDesc2')
        self.assertNotEqual(create_form.data['description'], edit_form.data['description'])
        self.assertEqual(create_form.files['file'], image1)
        self.assertEqual(edit_form.files['file'], image2)
        self.assertNotEqual(create_form.files['file'], edit_form.files['file'])
        self.assertTrue(edit_form.is_valid)


class TestPubCommentForm(CoreTestCase):
    def test_valid_form(self):
        data = {
            'comment': 'testComment',
            'obj_pk': self.pub.id,
        }
        form = PubCommentForm(data=data)
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_empty_objPK_field(self):
        data = {
            'comment': 'testComment',
            'obj_pk': '',
        }
        form = PubCommentForm(data=data)
        print(form.errors)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['obj_pk'], ['This field is required.'])
