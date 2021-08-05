from django.urls import path
from beer_collector.collector_profile.views import ProfileEditView, ProfileDetailsView
# Important
from beer_collector.core import signals

urlpatterns = [
    path('details/<int:pk>', ProfileDetailsView.as_view(), name='profile details'),
    path('edit/<int:pk>', ProfileEditView.as_view(), name='profile edit'),
]
