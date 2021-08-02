from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate, get_user_model, password_validation
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.core.exceptions import ValidationError

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
            }
        ),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'current-password',
                'placeholder': 'Enter your password',
                'style': 'width: 400px',
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
            }
        ),
    )
