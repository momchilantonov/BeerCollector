from django import forms
from django.contrib.auth import authenticate, get_user_model, password_validation
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError

UserModel = get_user_model()


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Enter your password',
                'style': 'width: 400px',
            }
        ),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
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
                    'placeholder': 'Enter your email address',
                    'style': 'width: 400px',
                }
            ),
        }


class SignInForm(AuthenticationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Enter your email address',
                'style': 'width: 400px',
            }
        ),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Enter your password',
                'style': 'width: 400px',
            }
        ),
    )

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            user = authenticate(username=email, password=password)
            if not user:
                raise ValidationError('Incorrect email!')
            if not user.check_password(password):
                raise ValidationError('Incorrect password!')
            if not user.is_active:
                raise ValidationError('This user is not active!')
        return super(SignInForm, self).clean()

    # def clean_password(self):
    #     self.user = authenticate(
    #         email=self.cleaned_data['email'],
    #         password=self.cleaned_data['password'],
    #     )
    #
    #     if not self.user:
    #         raise ValidationError('Email and/or password incorrect')
    #
    # def save(self):
    #     return self.user
