from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DeleteView, TemplateView
from beer_collector.account.forms import SignUpForm, SignInForm, ChangePasswordForm

UserModel = get_user_model()


class SignUpView(CreateView):
    template_name = 'auth/sign-up.html'
    model = UserModel
    form_class = SignUpForm
    success_url = reverse_lazy('sign up done')

    # OVERRIDE DEF FORM_VALID IF WE NEED TO LOGIN THE USER AFTER REGISTRATION
    # def form_valid(self, form):
    #     form.save()
    #     user = authenticate(
    #         username=form.cleaned_data["email"],
    #         password=form.cleaned_data["password1"],
    #     )
    #     login(self.request, user)
    #     return redirect('home page')


class SignUpDoneView(TemplateView):
    template_name = 'auth/sign-up-done.html'


class SignInView(LoginView):
    template_name = 'auth/sign-in.html'
    form_class = SignInForm

    def get_success_url(self):
        return reverse('home page')


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
        return reverse('delete account done')


class DeleteAccountDoneView(TemplateView):
    template_name = 'auth/delete-account-done.html'

# FBV VIEWS
# def sign_up(req):
#     if req.POST:
#         form = SignUpForm(req.POST)
#         if form.is_valid():
#             user = form.save()
#             login(req, user)
#             return redirect('home page')
#     else:
#         form = SignUpForm()
#
#     context = {
#         'form': form,
#     }
#
#     return render(req, 'auth/sign-up.html', context)
#
#
# def sign_in(req):
#     if req.POST:
#         form = SignInForm(req.POST)
#         if form.is_valid():
#             user = form.save()
#             login(req, user)
#             return redirect('home page')
#     else:
#         form = SignInForm()
#
#     context = {
#         'form': form,
#     }
#
#     return render(req, 'auth/sign-in.html', context)
#
#
# def sign_out(req):
#     logout(req)
#     return redirect('home page')
#
#
# def delete_account(req):
#     user = req.user
#     if req.POST:
#         user.delete()
#         return redirect('home page')
#     return render(req, 'auth/delete-account.html')
