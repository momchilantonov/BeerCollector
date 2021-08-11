import os
import tempfile
from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from beer_collector.beer.models.beer import Beer, BeerLike, BeerComment
from beer_collector.beer.models.beer_style import BeerStyle, BeerStyleLike, BeerStyleComment
from django.core.files.uploadedfile import SimpleUploadedFile

UserModel = get_user_model()


class CoreTestCase(TestCase):
    def setUp(self):
        # create client
        self.client = Client()

        # create large img for test img validator
        self.large_image_for_test = SimpleUploadedFile(
            name='large_image_test.jpg',
            content=open(os.path.join(settings.BASE_DIR, 'static/images/large_image_test.jpg'), 'rb').read(),
        )

        # create users
        user1_email = 'test1@test1.com'
        user1_password = 'test1234'
        self.user1 = UserModel.objects.create_user(
            email=user1_email,
            password=user1_password,
        )
        self.user1.is_active = True

        user2_email = 'test2@test2.com'
        user2_password = 'test5678'
        self.user2 = UserModel.objects.create_user(
            email=user2_email,
            password=user2_password,
        )
        self.user2.is_active = True

        user3_email = 'test3@test3.com'
        user3_password = 'test9012'
        self.user3 = UserModel.objects.create_user(
            email=user3_email,
            password=user3_password,
        )
        self.user3.is_active = True

        user4_email = 'test4@test4.com'
        user4_password = 'test3456'
        self.user4 = UserModel.objects.create_user(
            email=user4_email,
            password=user4_password,
        )
        self.user4.is_active = True

        # create beerStyle, comments and likes
        self.beer_style = BeerStyle.objects.create(
            type='testType',
            description='testDesc',
            user=self.user1,
        )

        self.beer_style_like1 = BeerStyleLike.objects.create(
            beer_style=self.beer_style,
            user=self.user2,
        )

        self.beer_style_like2 = BeerStyleLike.objects.create(
            beer_style=self.beer_style,
            user=self.user3,
        )

        self.beer_style_like3 = BeerStyleLike.objects.create(
            beer_style=self.beer_style,
            user=self.user4,
        )

        self.beer_style_likes = []
        self.beer_style_likes.extend(
            [
                self.beer_style_like1,
                self.beer_style_like2,
                self.beer_style_like3,
            ]
        )

        self.beer_style_comment1 = BeerStyleComment.objects.create(
            comment='Comment1',
            beer_style=self.beer_style,
            user=self.user2,
        )

        self.beer_style_comment2 = BeerStyleComment.objects.create(
            comment='Comment2',
            beer_style=self.beer_style,
            user=self.user3,
        )

        self.beer_style_comment3 = BeerStyleComment.objects.create(
            comment='Comment3',
            beer_style=self.beer_style,
            user=self.user4,
        )

        self.beer_style_comments = []
        self.beer_style_comments.extend(
            [
                self.beer_style_comment1,
                self.beer_style_comment2,
                self.beer_style_comment3,
            ]
        )

        # create beer, comments and likes
        self.beer = Beer.objects.create(
            label='testLabel',
            type=self.beer_style,
            description='testDesc',
            image=tempfile.NamedTemporaryFile(suffix="_test.jpg").name,
            user=self.user1,
        )

        self.beer_like1 = BeerLike.objects.create(
            beer=self.beer,
            user=self.user2,
        )

        self.beer_like2 = BeerLike.objects.create(
            beer=self.beer,
            user=self.user3,
        )

        self.beer_like3 = BeerLike.objects.create(
            beer=self.beer,
            user=self.user4,
        )

        self.beer_likes = []
        self.beer_likes.extend(
            [
                self.beer_like1,
                self.beer_like2,
                self.beer_like3,
            ]
        )

        self.beer_comment1 = BeerComment.objects.create(
            comment='Comment1',
            beer=self.beer,
            user=self.user2,
        )

        self.beer_comment2 = BeerComment.objects.create(
            comment='Comment2',
            beer=self.beer,
            user=self.user3,
        )

        self.beer_comment3 = BeerComment.objects.create(
            comment='Comment3',
            beer=self.beer,
            user=self.user4,
        )

        self.beer_comments = []
        self.beer_comments.extend(
            [
                self.beer_comment1,
                self.beer_comment2,
                self.beer_comment3,
            ]
        )