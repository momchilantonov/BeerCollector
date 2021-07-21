from django.urls import path
from beer_collector.collector_profile.views import profile_details, profile_edit
from beer_collector.collector_profile import signals


urlpatterns = [
    path('details/', profile_details, name='profile details'),
    path('edit/', profile_edit, name='profile edit'),
]
