from django.urls import path
from beer_collector.account.email_activation import activate_account
from beer_collector.account.views import (
    SignUpView, SuccessfulActivationDoneView, SignInView, SignOutView,
    ChangePasswordView, ChangePasswordDoneView, ResetForgottenPasswordView,
    ResetForgottenPasswordDoneView, ResetForgottenPasswordConfirmView,
    ResetForgottenPasswordComplete, DeleteAccountView, DeleteAccountDoneView,
)

urlpatterns = [
    path('sign-up/', SignUpView.as_view(), name='sign up'),
    path('activate/<uidb64>/<token>/', activate_account, name='activate'),
    path('activation-success/', SuccessfulActivationDoneView.as_view(), name='activation success'),
    path('sign-in/', SignInView.as_view(), name='sign in'),
    path('sign-out/', SignOutView.as_view(), name='sign out'),
    path('change-password/', ChangePasswordView.as_view(), name='change password'),
    path('change-paswword-done/', ChangePasswordDoneView.as_view(), name='change password done'),
    path('reset-forgotten-password/', ResetForgottenPasswordView.as_view(), name='reset_password'),
    path('reset-forgotten-password-done/', ResetForgottenPasswordDoneView.as_view(), name='password_reset_done'),
    path('reset-forgotten-password-confirm/<uidb64>/<token>/',
         ResetForgottenPasswordConfirmView.as_view(), name='password_reset_confirm'),
    path('reset-forgotten-password-complete/',
         ResetForgottenPasswordComplete.as_view(), name='password_reset_complete'),
    path('delete-account/<int:pk>', DeleteAccountView.as_view(), name='delete account'),
    path('delete-account-done/', DeleteAccountDoneView.as_view(), name='delete account done'),
]
