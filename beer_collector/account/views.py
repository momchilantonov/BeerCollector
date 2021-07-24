from django.contrib.auth import login, logout, get_user_model, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from beer_collector.account.forms import SignUpForm, SignInForm

UserModel = get_user_model()


def sign_up(req):
    if req.POST:
        form = SignUpForm(req.POST)
        if form.is_valid():
            user = form.save()
            login(req, user)
            return redirect('home page')
    else:
        form = SignUpForm()

    context = {
        'form': form,
    }

    return render(req, 'auth/sign-up.html', context)


def sign_in(req):
    if req.POST:
        form = SignInForm(req.POST)
        if form.is_valid():
            user = form.save()
            login(req, user)
            return redirect('home page')
    else:
        form = SignInForm()

    context = {
        'form': form,
    }

    return render(req, 'auth/sign-in.html', context)


def sign_out(req):
    logout(req)
    return redirect('home page')


# @login_required
def delete_account(req):
    user = req.user
    if req.POST:
        user.delete()
        return redirect('home page')
    return render(req, 'auth/delete-account.html')


class SignUpView(CreateView):
    template_name = 'auth/sign-up.html'
    model = UserModel
    form_class = SignUpForm
    success_url = reverse_lazy('home page')

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

    def get_success_url(self):
        return reverse('home page')
