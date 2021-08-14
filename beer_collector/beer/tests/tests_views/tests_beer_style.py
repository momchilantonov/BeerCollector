from django.urls import reverse
from beer_collector.beer.models.beer_style import BeerStyle, BeerStyleLike, BeerStyleComment
from beer_collector.core.tests.tests_core import CoreTestCase


class TestCreateBeerStyleView(CoreTestCase):
    def test_create_beerStyle_view_without_logIn_user(self):
        response = self.client.get(reverse('beer style create'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/auth/sign-in/?next=/beer/beer-style-create/')

    def test_create_beerStyle_view_with_logIn_user(self):
        self.client.force_login(self.user1)
        response = self.client.get(reverse('beer style create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'beer/beer_style/beer-style-create.html')
        self.assertContains(response, 'Create your new beer style')

    def test_successful_create_beerStyle(self):
        self.client.force_login(self.user2)
        data = {
            'type': 'type',
            'description': 'desc',
        }
        response = self.client.post(reverse('beer style create'), data)
        user_beer_styles_list = self.user2.beerstyle_set.all()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(user_beer_styles_list), 1)


class TestEditBeerStyleView(CoreTestCase):
    def test_edit_beerStyle_view(self):
        self.client.force_login(self.user1)
        response = self.client.get(reverse('beer style edit', args=(self.beer_style.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'beer/beer_style/beer-style-edit.html')
        self.assertContains(response, 'Edit your beer style')

    def test_success_edit_beerStyle(self):
        self.client.force_login(self.user1)
        data = {
            'type': 'new_type',
            'description': 'new_desc',
        }
        response = self.client.post(reverse('beer style edit', args=(self.beer_style.id,)), data)
        beer_style = BeerStyle.objects.first()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(beer_style.type, 'new_type')
        self.assertEqual(beer_style.description, 'new_desc')


class TestDeleteBeerStyleView(CoreTestCase):
    def test_delete_beerStyle_view(self):
        self.client.force_login(self.user1)
        response = self.client.get(reverse('beer style delete', args=(self.beer_style.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'beer/beer_style/beer-style-delete.html')
        self.assertContains(response, 'Are you sure you want to delete your beer style?')

    def test_confirm_delete_beerStyle(self):
        self.client.force_login(self.user1)
        response = self.client.post(reverse('beer style delete', args=(self.beer_style.id,)))
        user_beer_styles_list = self.user1.beerstyle_set.all()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(user_beer_styles_list), 0)
        self.assertRedirects(response, reverse('beer style delete done'))

    def test_cancel_delete_beerStyle(self):
        self.client.force_login(self.user1)
        data = {
            'No': 'No'
        }
        response = self.client.post(reverse('beer style delete', args=(self.beer_style.id,)), data)
        user_beer_styles_list = self.user1.beerstyle_set.all()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(user_beer_styles_list), 1)


class TestDeleteBeerStyleDoneView(CoreTestCase):
    def test_delete_done_view(self):
        response = self.client.get(reverse('beer style delete done'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'beer/beer_style/beer-style-delete-done.html')
        self.assertContains(response, 'You have successfully delete your beer style!')


class TestBeerStyleListView(CoreTestCase):
    def test_beerStyle_list_view(self):
        response = self.client.get(reverse('beer style list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'beer/beer_style/beer-style-list.html')
        self.assertContains(response, 'Add new beer style')


class TestBeerStyleUserListView(CoreTestCase):
    def test_beerStyle_list_user_view(self):
        self.client.force_login(self.user1)
        response = self.client.get(reverse('beer style user list'))
        user_beer_styles_list = self.user1.beerstyle_set.all()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(user_beer_styles_list), 1)


class TestBeerStyleDetails(CoreTestCase):
    def test_beerStyle_details_view_without_logIn_user(self):
        response = self.client.get(reverse('beer style details', args=(self.beer_style.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'beer/beer_style/beer-style-details.html')
        self.assertFalse(response.context['is_owner'])
        self.assertFalse(response.context['is_liked'])
        self.assertNotContains(response, 'Edit')
        self.assertNotContains(response, 'Delete')

    def test_beerStyle_details_view_with_logIn_user_owner(self):
        self.client.force_login(self.user1)
        response = self.client.get(reverse('beer style details', args=(self.beer_style.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'beer/beer_style/beer-style-details.html')
        self.assertTrue(response.context['is_owner'])
        self.assertFalse(response.context['is_liked'])
        self.assertContains(response, 'Edit')
        self.assertContains(response, 'Delete')

    def test_beerStyle_details_view_with_logIn_user_no_owner(self):
        self.client.force_login(self.user2)
        response = self.client.get(reverse('beer style details', args=(self.beer_style.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'beer/beer_style/beer-style-details.html')
        self.assertFalse(response.context['is_owner'])
        self.assertTrue(response.context['is_liked'])
        self.assertNotContains(response, 'Edit')
        self.assertNotContains(response, 'Delete')


class TestBeerStyleLikeView(CoreTestCase):
    def test_like_beerStyle(self):
        self.client.force_login(self.user1)
        new_beer_style = BeerStyle.objects.create(
            type='type',
            description='typeDesc',
            user=self.user2,
        )
        response = self.client.post(reverse('beer style like', args=(new_beer_style.id,)))
        beer_style_like_exist = BeerStyleLike.objects.filter(user=self.user1, beer_style=new_beer_style).exists()
        self.assertEqual(response.status_code, 302)
        self.assertTrue(beer_style_like_exist)

    def test_dislike_beerStyle(self):
        self.client.force_login(self.user2)
        response = self.client.post(reverse('beer style like', args=(self.beer_style.id,)))
        beer_style_like_exist = BeerStyleLike.objects.filter(user=self.user1, beer_style=self.beer_style).exists()
        self.assertEqual(response.status_code, 302)
        self.assertFalse(beer_style_like_exist)


class TestBeerStyleCommentView(CoreTestCase):
    def test_add_comment_with_logIn_user(self):
        self.client.force_login(self.user2)
        beer_style_comment = self.beer_style_comment1
        response = self.client.post(reverse('beer style comment', args=(self.user2.id,)))
        beer_style_comments_count = self.beer_style.beerstylecomment_set.filter(user=self.user2).count()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(beer_style_comment.comment, 'Comment1')
        self.assertEqual(beer_style_comments_count, 1)

    def test_add_comment_without_logIn_user(self):
        BeerStyleComment.objects.create(
            comment='testComment',
            beer_style=self.beer_style,
            user=self.user2
        )
        response = self.client.post(reverse('beer style comment', args=(self.user2.id,)))
        self.assertEqual(response.status_code, 302)
