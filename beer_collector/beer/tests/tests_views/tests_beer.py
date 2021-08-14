import tempfile
from django.urls import reverse
from beer_collector.beer.models.beer import Beer, BeerLike, BeerComment
from beer_collector.core.tests.tests_core import CoreTestCase


class TestCreateBeerView(CoreTestCase):
    def test_create_beer_view_without_logIn_user(self):
        response = self.client.get(reverse('beer create'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/auth/sign-in/?next=/beer/beer-create/')

    def test_create_beer_view_with_logIn_user(self):
        self.client.force_login(self.user1)
        response = self.client.get(reverse('beer create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'beer/beer/beer-create.html')
        self.assertContains(response, 'Create your new beer')

    def test_successful_create_beer(self):
        self.client.force_login(self.user1)
        data = {
            'label': 'testLabel',
            'type': self.beer_style,
            'description': 'testDesc',
            'image': tempfile.NamedTemporaryFile(suffix="_test.jpg").name,
        }
        response = self.client.post(reverse('beer create'), data)
        user_beer_list = self.user1.beer_set.all()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(user_beer_list), 1)


class TestEditBeerView(CoreTestCase):
    def test_edit_beer_view(self):
        self.client.force_login(self.user1)
        response = self.client.get(reverse('beer edit', args=(self.beer.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'beer/beer/beer-edit.html')
        self.assertContains(response, 'Edit your beer')


class TestDeleteBeerView(CoreTestCase):
    def test_delete_beer_view(self):
        self.client.force_login(self.user1)
        response = self.client.get(reverse('beer delete', args=(self.beer.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'beer/beer/beer-delete.html')
        self.assertContains(response, 'Are you sure you want to delete your beer?')

    def test_confirm_delete_beerStyle(self):
        self.client.force_login(self.user1)
        response = self.client.post(reverse('beer delete', args=(self.beer.id,)))
        user_beer_list = self.user1.beer_set.all()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(user_beer_list), 0)
        self.assertRedirects(response, reverse('beer delete done'))

    def test_cancel_delete_beerStyle(self):
        self.client.force_login(self.user1)
        data = {
            'No': 'No'
        }
        response = self.client.post(reverse('beer delete', args=(self.beer.id,)), data)
        user_beer_list = self.user1.beer_set.all()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(user_beer_list), 1)


class TestDeleteBeerDoneView(CoreTestCase):
    def test_delete_done_view(self):
        response = self.client.get(reverse('beer delete done'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'beer/beer/beer-delete-done.html')
        self.assertContains(response, 'You have successfully delete your beer!')


class TestBeerListView(CoreTestCase):
    def test_beer_list_view(self):
        response = self.client.get(reverse('beer list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'beer/beer/beer-list.html')
        self.assertContains(response, 'Add new beer')


class TestBeerUserListView(CoreTestCase):
    def test_beer_list_user_view(self):
        self.client.force_login(self.user1)
        response = self.client.get(reverse('beer user list'))
        user_beer_list = self.user1.beer_set.all()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(user_beer_list), 1)


class TestBeerDetails(CoreTestCase):
    def test_beer_details_view_without_logIn_user(self):
        response = self.client.get(reverse('beer details', args=(self.beer.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'beer/beer/beer-details.html')
        self.assertFalse(response.context['is_owner'])
        self.assertFalse(response.context['is_liked'])
        self.assertNotContains(response, 'Edit')
        self.assertNotContains(response, 'Delete')

    def test_beer_details_view_with_logIn_user_owner(self):
        self.client.force_login(self.user1)
        response = self.client.get(reverse('beer details', args=(self.beer.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'beer/beer/beer-details.html')
        self.assertTrue(response.context['is_owner'])
        self.assertFalse(response.context['is_liked'])
        self.assertContains(response, 'Edit')
        self.assertContains(response, 'Delete')

    def test_beer_details_view_with_logIn_user_no_owner(self):
        self.client.force_login(self.user2)
        response = self.client.get(reverse('beer details', args=(self.beer.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'beer/beer/beer-details.html')
        self.assertFalse(response.context['is_owner'])
        self.assertTrue(response.context['is_liked'])
        self.assertNotContains(response, 'Edit')
        self.assertNotContains(response, 'Delete')


class TestBeerLikeView(CoreTestCase):
    def test_like_beer(self):
        self.client.force_login(self.user1)
        new_beer = Beer.objects.create(
            label='myLabel',
            type=self.beer_style,
            description='myDesc',
            image=tempfile.NamedTemporaryFile(suffix="_test.jpg").name,
            user=self.user2,
        )
        response = self.client.post(reverse('beer like', args=(new_beer.id,)))
        beer_like_exist = BeerLike.objects.filter(user=self.user1, beer=new_beer).exists()
        self.assertEqual(response.status_code, 302)
        self.assertTrue(beer_like_exist)

    def test_dislike_beer(self):
        self.client.force_login(self.user2)
        response = self.client.post(reverse('beer like', args=(self.beer.id,)))
        beer_like_exist = BeerLike.objects.filter(user=self.user1, beer=self.beer).exists()
        self.assertEqual(response.status_code, 302)
        self.assertFalse(beer_like_exist)


class TestBeerCommentView(CoreTestCase):
    def test_add_comment_with_logIn_user(self):
        self.client.force_login(self.user2)
        beer_comment = self.beer_comment1
        response = self.client.post(reverse('beer comment', args=(self.user2.id,)))
        beer_comments_count = self.beer.beercomment_set.filter(user=self.user2).count()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(beer_comment.comment, 'Comment1')
        self.assertEqual(beer_comments_count, 1)

    def test_add_comment_without_logIn_user(self):
        BeerComment.objects.create(
            comment='testComment',
            beer=self.beer,
            user=self.user2
        )
        response = self.client.post(reverse('beer comment', args=(self.user2.id,)))
        self.assertEqual(response.status_code, 302)
