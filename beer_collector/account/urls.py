from django.urls import path
from beer_collector.account.views import (
    SignUpView, SignInView, SignOutView, ChangePasswordView,
    DeleteAccountView, ChangePasswordDoneView, DeleteAccountDoneView,
)

urlpatterns = [
    path('sign-up/', SignUpView.as_view(), name='sign up'),
    path('sign-in/', SignInView.as_view(), name='sign in'),
    path('sign-out/', SignOutView.as_view(), name='sign out'),
    path('change-password/', ChangePasswordView.as_view(), name='change password'),
    path('change-paswword-done/', ChangePasswordDoneView.as_view(), name='change password done'),
    path('delete-account/<int:pk>', DeleteAccountView.as_view(), name='delete account'),
    path('delete-account-done/', DeleteAccountDoneView.as_view(), name='delete account done'),
]
