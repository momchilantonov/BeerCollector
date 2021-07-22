from django.urls import path
from beer_collector.account.views import sign_up, sign_in, sign_out, delete_account

urlpatterns = [
    path('sign-up/', sign_up, name='sign up'),
    path('sign-in/', sign_in, name='sign in'),
    path('sign-out/', sign_out, name='sign out'),
    path('delete-account', delete_account, name='delete account'),
]
