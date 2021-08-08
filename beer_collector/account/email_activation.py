from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import render
from django.utils.http import urlsafe_base64_decode
from beer_collector.account.forms import SignInForm

UserModel = get_user_model()


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
