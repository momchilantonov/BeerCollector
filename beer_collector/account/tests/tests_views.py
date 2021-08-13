from beer_collector.core.tests.tests_core import CoreTestCase
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib import auth
from django.core import mail

UserModel = get_user_model()


class TestSignUpView(CoreTestCase):
    def test_signUp_before_activation(self):
        self.user1.is_active = False
        self.assertTrue(isinstance(self.user1, UserModel))
        self.assertEqual('test1@test1.com', self.user1.email)
        self.assertTrue(not self.user1.is_active)

    def test_signUp_after_activation(self):
        self.assertTrue(isinstance(self.user1, UserModel))
        self.assertEqual('test1@test1.com', self.user1.email)
        self.assertTrue(self.user1.is_active)

    def test_send_email_for_verification(self):
        email = EmailMessage(
            from_email=self.user1.email,
            to=('rec@rec.com',),
            subject='Test message',
            body='This is a test email',
        )
        email.send()
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].from_email, self.user1.email)
        self.assertEqual(mail.outbox[0].to, ['rec@rec.com'])
        self.assertEqual(mail.outbox[0].subject, 'Test message')
        self.assertEqual(mail.outbox[0].body, 'This is a test email')


class TestSuccessfulActivationDoneView(CoreTestCase):
    def test_activation_done(self):
        response = self.client.get(reverse('activation success'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'auth/account-activate-done.html')
        self.assertContains(response, 'You have successfully activate your registration!')


class TestSighInView(CoreTestCase):
    def test_get_signIn_view(self):
        response = self.client.get(reverse('sign in'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Please fill all the fields to Sign In')

    def test_successful_signIn(self):
        self.client.login(username='test1@test1.com', password='test1234')
        user = auth.get_user(self.client)
        data = {'user': user}
        response = self.client.post(reverse('sign in'), data)
        self.assertTrue(user.is_authenticated)
        self.assertEqual(response.status_code, 302)

    def test_unsuccessful_signIn(self):
        self.client.login(email='a@a.bg', password='qwer1234')
        user = auth.get_user(self.client)
        data = {'user': user}
        response = self.client.post(reverse('sign in'), data)
        self.assertTrue(not user.is_authenticated)
        self.assertEqual(response.status_code, 200)


class TestSignOutView(CoreTestCase):
    def test_successful_signOut(self):
        self.client.force_login(self.user1)
        self.client.logout()
        response = self.client.post(reverse('sign out'))
        self.assertEqual(response.status_code, 302)


class TestChangePasswordView(CoreTestCase):
    def test_change_password_view(self):
        self.client.force_login(self.user1)
        response = self.client.get(reverse('change password'))
        self.assertEqual(response.status_code, 200)

    def test_successful_change_password(self):
        self.client.force_login(self.user1)
        self.user1.set_password('new_password')
        self.user1.save()
        data = {'user': self.user1}
        response = self.client.post(reverse('change password'), data)
        self.assertTrue(self.user1.check_password('new_password'))
        self.assertEqual(response.status_code, 302)


class TestChangePasswordDoneView(CoreTestCase):
    def test_change_password_done_view(self):
        self.client.force_login(self.user1)
        response = self.client.get(reverse('change password done'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'You have successfully changed your password!')


class TestDeleteAccountView(CoreTestCase):
    def test_delete_account_view(self):
        self.client.force_login(self.user1)
        response = self.client.get(reverse('delete account', args=(self.user1.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Are you sure you want to delete your profile?')

    def test_successful_delete_account(self):
        self.client.force_login(self.user1)
        response = self.client.post(reverse('delete account', args=(self.user1.id,)))
        self.assertEqual(response.status_code, 302)
