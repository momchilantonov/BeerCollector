from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from beer_collector.account.forms import SignUpForm, SignInForm


def sign_up(req):
    if req.POST:
        form = SignUpForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('sign in')
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


@login_required
def delete_account(req):
    pass
