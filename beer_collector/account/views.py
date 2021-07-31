from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth import get_user_model, logout, authenticate, login
from django.views.generic import CreateView, DeleteView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from beer_collector.account.forms import SignUpForm, SignInForm, ChangePasswordForm

UserModel = get_user_model()


class SignUpView(CreateView):
    template_name = 'auth/sign-up.html'
    model = UserModel
    form_class = SignUpForm

    def form_valid(self, form):
        form.save()
        user = authenticate(
            username=form.cleaned_data["email"],
            password=form.cleaned_data["password1"],
        )
        login(self.request, user)
        return redirect('home page')


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


class ChangePasswordDoneView(TemplateView):
    template_name = 'auth/change-password-done.html'


class DeleteAccountView(DeleteView):
    model = UserModel
    template_name = 'auth/delete-account.html'

    def get_success_url(self):
        logout(self.request)
        return reverse('delete account done')


class DeleteAccountDoneView(TemplateView):
    template_name = 'auth/delete-account-done.html'
