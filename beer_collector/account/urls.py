from django.urls import path
from beer_collector.account.views import (
    # sign_up, sign_in, sign_out, delete_account,
    SignUpView, SignInView, SignOutView, ChangePasswordView,
    ChangePasswordDoneView, DeleteAccountView, DeleteAccountDoneView, SignUpDoneView,
)

urlpatterns = [
    # path('sign-up/', sign_up, name='sign up'),
    # path('sign-in/', sign_in, name='sign in'),
    # path('sign-out/', sign_out, name='sign out'),
    # path('delete-account/', delete_account, name='delete account'),
    path('sign-up/', SignUpView.as_view(), name='sign up'),
    path('sign-up-done/', SignUpDoneView.as_view(), name='sign up done'),
    path('sign-in/', SignInView.as_view(), name='sign in'),
    path('sign-out/', SignOutView.as_view(), name='sign out'),
    path('change-password/', ChangePasswordView.as_view(), name='change password'),
    path('change-paswword-done/', ChangePasswordDoneView.as_view(), name='change password done'),
    path('delete-account/<int:pk>', DeleteAccountView.as_view(), name='delete account'),
    path('delete-account-done/', DeleteAccountDoneView.as_view(), name='delete account done'),
]
