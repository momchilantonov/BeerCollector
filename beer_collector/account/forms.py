from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate, get_user_model, password_validation
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import (
    UserCreationForm, AuthenticationForm, PasswordChangeForm,
    SetPasswordForm, PasswordResetForm,
)

UserModel = get_user_model()


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password',
                'placeholder': 'Enter your password',
                'style': 'width: 400px',
                'class': 'form-control',
            }
        ),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password',
                'placeholder': 'Confirm your password',
                'style': 'width: 400px',
                'class': 'form-control',
            }
        ),
        help_text=password_validation.password_validators_help_text_html(),
    )

    class Meta:
        model = UserModel
        fields = (
            'email',
        )
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Enter valid email address',
                    'style': 'width: 400px',
                    'class': 'form-control',
                }
            ),
        }


class SignInForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__(*args, **kwargs)

    username = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'autofocus': True,
                'placeholder': 'Enter valid email address',
                'style': 'width: 400px',
                'class': 'form-control',
            }
        ),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'current-password',
                'placeholder': 'Enter your password',
                'style': 'width: 400px',
                'class': 'form-control',
            }
        ),
    )

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise ValidationError('Incorrect email and/or password!')
        return super(SignInForm, self).clean()

    def save(self):
        return self.user


class ChangePasswordForm(PasswordChangeForm, SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

    old_password = forms.CharField(
        label=_("Old password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Enter your old password',
                'style': 'width: 400px',
                'class': 'form-control',
            }
        ),
    )
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password',
                'placeholder': 'Enter your new password',
                'style': 'width: 400px',
                'class': 'form-control',
            }
        ),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password',
                'placeholder': 'Confirm your new password',
                'style': 'width: 400px',
                'class': 'form-control',
            }
        ),
    )


class ResetForgottenPasswordForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(ResetForgottenPasswordForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(
            attrs={
                'autocomplete': 'email',
                'placeholder': 'Enter your email address',
                'style': 'width: 400px',
                'class': 'form-control',
            }
        ),
    )


class SetForgottenPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(SetForgottenPasswordForm, self).__init__(*args, **kwargs)

    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password',
                'placeholder': 'Enter your new password',
                'style': 'width: 400px',
                'class': 'form-control',
            }
        ),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password',
                'placeholder': 'Confirm your new password',
                'style': 'width: 400px',
                'class': 'form-control',
            }
        ),
    )
