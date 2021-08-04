from django.urls import path
from beer_collector.account.views import (
    SignUpView, activate_account, SignInView, SignOutView, SuccessfulActivationDone,
    ChangePasswordView, ResetForgottenPasswordView, DeleteAccountView, DeleteAccountDoneView,
    ChangePasswordDoneView, ConfirmResetPasswordView,
)

urlpatterns = [
    path('sign-up/', SignUpView.as_view(), name='sign up'),
    path('activate/<uidb64>/<token>/', activate_account, name='activate'),
    path('activation-success/', SuccessfulActivationDone.as_view(), name='activation success'),
    path('sign-in/', SignInView.as_view(), name='sign in'),
    path('sign-out/', SignOutView.as_view(), name='sign out'),
    path('change-password/', ChangePasswordView.as_view(), name='change password'),
    path('change-paswword-done/', ChangePasswordDoneView.as_view(), name='change password done'),
    path('reset-forgotten-password/', ResetForgottenPasswordView.as_view(), name='reset forgotten password'),
    path('confirm-forgotten-password/<uidb64>/<token>/', ConfirmResetPasswordView.as_view(), name='confirm forgotten password'),
    path('delete-account/<int:pk>', DeleteAccountView.as_view(), name='delete account'),
    path('delete-account-done/', DeleteAccountDoneView.as_view(), name='delete account done'),
]
