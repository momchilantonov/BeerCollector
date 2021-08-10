from django.test import TestCase
from beer_collector.account.forms import SignUpForm, SignInForm, ChangePasswordForm, SetForgottenPasswordForm
from beer_collector.core.tests.core import CoreTestCase


class TestSignUpForm(TestCase):
    def test_valid_form(self):
        data = {
            'email': 'test@test.com',
            'password1': 'HardTest1234',
            'password2': 'HardTest1234',
        }
        form = SignUpForm(data=data)
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_empty_form(self):
        data = {}
        form = SignUpForm(data=data)
        print(form.errors)
        self.assertEqual(form.errors['email'], ['This field is required.'])
        self.assertEqual(form.errors['password1'], ['This field is required.'])
        self.assertEqual(form.errors['password2'], ['This field is required.'])
        self.assertFalse(form.is_valid())

    def test_common_password(self):
        data = {
            'email': 'test@test.com',
            'password1': 'test1234',
            'password2': 'test1234',
        }
        form = SignUpForm(data=data)
        print(form.errors)
        self.assertEqual(form.errors['password2'], ['This password is too common.'])
        self.assertFalse(form.is_valid())

    def test_password_similar_to_email(self):
        data = {
            'email': 'test@test.com',
            'password1': 'test@test.com',
            'password2': 'test@test.com',
        }
        form = SignUpForm(data=data)
        print(form.errors)
        self.assertEqual(form.errors['password2'], ['The password is too similar to the email address.'])
        self.assertFalse(form.is_valid())

    def test_short_password(self):
        data = {
            'email': 'test@test.com',
            'password1': 'AbcCba',
            'password2': 'AbcCba',
        }
        form = SignUpForm(data=data)
        print(form.errors)
        self.assertEqual(form.errors['password2'],
                         ['This password is too short. It must contain at least 8 characters.'])
        self.assertFalse(form.is_valid())

    def test_only_digits_password(self):
        data = {
            'email': 'test@test.com',
            'password1': '1236521578932145',
            'password2': '1236521578932145',
        }
        form = SignUpForm(data=data)
        print(form.errors)
        self.assertEqual(form.errors['password2'], ['This password is entirely numeric.'])
        self.assertFalse(form.is_valid())

    def test_different_passwords(self):
        data = {
            'email': 'test@test.com',
            'password1': 'MegaTurbo1234',
            'password2': 'MegaTurbo5678',
        }
        form = SignUpForm(data=data)
        print(form.errors)
        self.assertEqual(form.errors['password2'], ['The two password fields didn’t match.'])
        self.assertFalse(form.is_valid())

    def test_invalid_email(self):
        data = {
            'email': 'test.com',
            'password1': 'MegaTurbo1234',
            'password2': 'MegaTurbo1234',
        }
        form = SignUpForm(data=data)
        print(form.errors)
        self.assertEqual(form.errors['email'], ['Enter a valid email address.'])
        self.assertFalse(form.is_valid())


class TestSignInForm(CoreTestCase):
    def test_valid_form(self):
        data = {
            'username': 'test1@test1.com',
            'password': 'test1234',
        }
        form = SignInForm(data=data)
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_empty_form(self):
        data = {}
        form = SignInForm(data=data)
        print(form.errors)
        self.assertEqual(form.errors['username'], ['This field is required.'])
        self.assertEqual(form.errors['password'], ['This field is required.'])
        self.assertFalse(form.is_valid())

    def test_empty_username_field(self):
        data = {
            'password': 'test1234'
        }
        form = SignInForm(data=data)
        print(form.errors)
        self.assertEqual(form.errors['username'], ['This field is required.'])
        self.assertFalse(form.is_valid())

    def test_empty_password_field(self):
        data = {
            'username': 'test1@test1.com',
        }
        form = SignInForm(data=data)
        print(form.errors)
        self.assertEqual(form.errors['password'], ['This field is required.'])
        self.assertFalse(form.is_valid())

    def test_invalid_email_credential(self):
        data = {
            'username': 'test@abv.bg',
            'password': 'test1234',
        }
        form = SignInForm(data=data)
        print(form.errors)
        self.assertEqual(form.errors['username'], ['Incorrect email.'])
        self.assertFalse(form.is_valid())

    def test_invalid_password_credential(self):
        data = {
            'username': 'test1@test1.com',
            'password': 'test5678',
        }
        form = SignInForm(data=data)
        print(form.errors)
        self.assertEqual(form.errors['password'], ['Incorrect password.'])
        self.assertFalse(form.is_valid())

    def test_inActive_account(self):
        self.user1.is_active = False
        self.user1.save()
        data = {
            'username': 'test1@test1.com',
            'password': 'test1234',
        }
        form = SignInForm(data=data)
        print(form.errors)
        self.assertEqual(form.errors['username'], ['Inactive account.'])
        self.assertFalse(form.is_valid())


class TestChangePasswordForm(CoreTestCase):
    def test_valid_form(self):
        data = {
            'old_password': 'test1234',
            'new_password1': 'MegaHard1234',
            'new_password2': 'MegaHard1234',
        }
        form = ChangePasswordForm(data=data, user=self.user1)
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_empty_form(self):
        data = {}
        form = ChangePasswordForm(data=data, user=self.user1)
        print(form.errors)
        self.assertEqual(form.errors['old_password'], ['This field is required.'])
        self.assertEqual(form.errors['new_password1'], ['This field is required.'])
        self.assertEqual(form.errors['new_password2'], ['This field is required.'])
        self.assertFalse(form.is_valid())

    def test_invalid_oldPassword(self):
        data = {
            'old_password': 'test5678',
            'new_password1': 'MegaHard1234',
            'new_password2': 'MegaHard1234',
        }
        form = ChangePasswordForm(data=data, user=self.user1)
        print(form.errors)
        self.assertEqual(form.errors['old_password'],
                         ['Your old password was entered incorrectly. Please enter it again.'])
        self.assertFalse(form.is_valid())

    def test_different_newPasswords(self):
        data = {
            'old_password': 'test1234',
            'new_password1': 'Mega1234',
            'new_password2': 'MegaHard1234',
        }
        form = ChangePasswordForm(data=data, user=self.user1)
        print(form.errors)
        self.assertEqual(form.errors['new_password2'], ['The two password fields didn’t match.'])
        self.assertFalse(form.is_valid())


class TestSetForgottenPasswordForm(CoreTestCase):
    def test_valid_form(self):
        data = {
            'new_password1': 'test5678',
            'new_password2': 'test5678',
        }
        form = SetForgottenPasswordForm(data=data, user=self.user1)
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_different_newPasswords(self):
        self.user1.save()
        data = {
            'new_password1': 'Pass9012',
            'new_password2': 'Pass5678',
        }
        form = SetForgottenPasswordForm(data=data, user=self.user1)
        print(form.errors)
        self.assertEqual(form.errors['new_password2'], ['The two password fields didn’t match.'])
        self.assertFalse(form.is_valid())
