from django.urls import path
from beer_collector.collector_profile.views import profile_details
from beer_collector.collector_profile import signals


urlpatterns = [
    path('', profile_details, name='profile details')
]
