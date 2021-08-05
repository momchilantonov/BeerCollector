from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.contrib.auth import get_user_model, logout
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import CreateView, DeleteView, TemplateView
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView,
    PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView,
)
from beer_collector.account.forms import (
    SignUpForm, SignInForm, ChangePasswordForm,
    ResetForgottenPasswordForm, SetForgottenPasswordForm,
)

UserModel = get_user_model()


class SignUpView(CreateView):
    template_name = 'auth/sign-up.html'
    model = UserModel
    form_class = SignUpForm

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        current_site = get_current_site(self.request)
        mail_subject = 'Activate your account.'
        message = render_to_string('auth/account_activate_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),
        })
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(
            mail_subject,
            message,
            to=[to_email],
        )
        email.send()
        return render(self.request, 'auth/account_activation_needed.html')


def activate_account(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        context = {
            'form': SignInForm,
        }
        user.is_active = True
        user.save()
        return render(request, 'auth/account-activate-done.html', context)
    else:
        return render(request, 'auth/account_activation_invalid.html')


class SuccessfulActivationDone(TemplateView):
    template_name = ''


class SignInView(LoginView):
    template_name = 'auth/sign-in.html'
    form_class = SignInForm
    redirect_authenticated_user = True
    redirect_field_name = 'next'


class SignOutView(LogoutView):
    pass


class ChangePasswordView(PasswordChangeView):
    template_name = 'auth/change-password.html'
    form_class = ChangePasswordForm
    success_url = reverse_lazy('change password done')


class ChangePasswordDoneView(PasswordChangeDoneView):
    template_name = 'auth/change-password-done.html'


class ResetForgottenPasswordView(PasswordResetView):
    template_name = 'auth/reset-password.html'
    form_class = ResetForgottenPasswordForm


class ResetForgottenPasswordDoneView(PasswordResetDoneView):
    template_name = 'auth/reset-password-done.html'


class ResetForgottenPasswordConfirmView(PasswordResetConfirmView):
    template_name = 'auth/reset-password-confirm.html'
    form_class = SetForgottenPasswordForm


class ResetForgottenPasswordComplete(PasswordResetCompleteView):
    template_name = 'auth/reset-password-complete.html'


class DeleteAccountView(DeleteView):
    model = UserModel
    template_name = 'auth/delete-account.html'

    def get_success_url(self):
        logout(self.request)
        return reverse('delete account done')


class DeleteAccountDoneView(TemplateView):
    template_name = 'auth/delete-account-done.html'
