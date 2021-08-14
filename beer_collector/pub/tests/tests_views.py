import tempfile

from django.urls import reverse

from beer_collector.core.tests.tests_core import CoreTestCase
from beer_collector.pub.models import Pub, PubLike, PubComment


class TestCreatePubView(CoreTestCase):
    def test_create_pub_view_without_logIn_user(self):
        response = self.client.get(reverse('pub create'))
        self.assertEqual(response.status_code, 302)

    def test_create_pub_view_with_logIn_user(self):
        self.client.force_login(self.user1)
        response = self.client.get(reverse('pub create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pub/pub-create.html')
        self.assertContains(response, 'Create your new pub')

    def test_successful_create_pub(self):
        self.client.force_login(self.user1)
        data = {
            'name': 'testPub1',
            'address': 'testAddress1',
            'description': 'testDesc1',
            'website': 'https://www.test1.com/',
            'image': tempfile.NamedTemporaryFile(suffix="_test.jpg").name,
            'longitude': 23.111111,
            'latitude': 41.000000,
        }
        response = self.client.post(reverse('pub create'), data)
        user_pub_list = self.user1.pub_set.all()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(user_pub_list), 2)


class TestEditPubView(CoreTestCase):
    def test_edit_beer_view(self):
        self.client.force_login(self.user1)
        response = self.client.get(reverse('pub edit', args=(self.pub.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pub/pub-edit.html')
        self.assertContains(response, 'Edit your pub')


class TestDeletePubView(CoreTestCase):
    def test_delete_pub_view(self):
        self.client.force_login(self.user1)
        response = self.client.get(reverse('pub delete', args=(self.pub.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pub/pub-delete.html')
        self.assertContains(response, 'Are you sure you want to delete your pub?')

    def test_confirm_delete_pub(self):
        self.client.force_login(self.user1)
        response = self.client.post(reverse('pub delete', args=(self.pub.id,)))
        user_pub_list = self.user1.pub_set.all()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(user_pub_list), 0)
        self.assertRedirects(response, reverse('pub delete done'))

    def test_cancel_delete_pub(self):
        self.client.force_login(self.user1)
        data = {
            'No': 'No'
        }
        response = self.client.post(reverse('pub delete', args=(self.pub.id,)), data)
        user_pub_list = self.user1.pub_set.all()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(user_pub_list), 1)


class TestDeletePubDoneView(CoreTestCase):
    def test_delete_done_view(self):
        response = self.client.get(reverse('pub delete done'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pub/pub-delete-done.html')
        self.assertContains(response, 'You have successfully delete your pub!')


class TestPubListView(CoreTestCase):
    def test_pub_list_view(self):
        response = self.client.get(reverse('pub list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pub/pub-list.html')
        self.assertContains(response, 'Add new pub')


class TestPubUserListView(CoreTestCase):
    def test_pub_list_user_view(self):
        self.client.force_login(self.user1)
        response = self.client.get(reverse('pub user list'))
        user_pub_list = self.user1.beer_set.all()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(user_pub_list), 1)


class TestPubDetails(CoreTestCase):
    def test_pub_details_view_without_logIn_user(self):
        response = self.client.get(reverse('pub details', args=(self.pub.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pub/pub-details.html')
        self.assertFalse(response.context['is_owner'])
        self.assertFalse(response.context['is_liked'])
        self.assertNotContains(response, 'Edit')
        self.assertNotContains(response, 'Delete')

    def test_pub_details_view_with_logIn_user_owner(self):
        self.client.force_login(self.user1)
        response = self.client.get(reverse('pub details', args=(self.pub.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pub/pub-details.html')
        self.assertTrue(response.context['is_owner'])
        self.assertFalse(response.context['is_liked'])
        self.assertContains(response, 'Edit')
        self.assertContains(response, 'Delete')

    def test_pub_details_view_with_logIn_user_no_owner(self):
        self.client.force_login(self.user2)
        response = self.client.get(reverse('pub details', args=(self.beer.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pub/pub-details.html')
        self.assertFalse(response.context['is_owner'])
        self.assertTrue(response.context['is_liked'])
        self.assertNotContains(response, 'Edit')
        self.assertNotContains(response, 'Delete')


class TestPubLikeView(CoreTestCase):
    def test_like_pub(self):
        self.client.force_login(self.user1)
        new_pub = Pub.objects.create(
            name='testPub2',
            address='testAddress2',
            description='testDesc2',
            website='https://www.test2.com/',
            image=tempfile.NamedTemporaryFile(suffix="_test.jpg").name,
            longitude=23.000000,
            latitude=41.111111,
            user=self.user2,
        )
        response = self.client.post(reverse('pub like', args=(new_pub.id,)))
        pub_like_exist = PubLike.objects.filter(user=self.user1, pub=new_pub).exists()
        self.assertEqual(response.status_code, 302)
        self.assertTrue(pub_like_exist)

    def test_dislike_pub(self):
        self.client.force_login(self.user2)
        response = self.client.post(reverse('pub like', args=(self.pub.id,)))
        pub_like_exist = PubLike.objects.filter(user=self.user1, pub=self.pub).exists()
        self.assertEqual(response.status_code, 302)
        self.assertFalse(pub_like_exist)


class TestPubCommentView(CoreTestCase):
    def test_add_comment_with_logIn_user(self):
        self.client.force_login(self.user2)
        pub_comment = self.pub_comment1
        response = self.client.post(reverse('pub comment', args=(self.user2.id,)))
        pub_comments_count = self.pub.pubcomment_set.filter(user=self.user2).count()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(pub_comment.comment, 'Comment1')
        self.assertEqual(pub_comments_count, 1)

    def test_add_comment_without_logIn_user(self):
        PubComment.objects.create(
            comment='testComment',
            pub=self.pub,
            user=self.user2
        )
        response = self.client.post(reverse('pub comment', args=(self.user2.id,)))
        self.assertEqual(response.status_code, 302)
