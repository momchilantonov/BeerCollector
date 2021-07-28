from beer_collector.collector_profile import signals
from django.urls import path
from beer_collector.collector_profile.views import (
    # profile_details, profile_edit,
    ProfileEditView, ProfileDetailsView, ProfileEditDoneView,
)

urlpatterns = [
    # path('details/', profile_details, name='profile details'),
    # path('edit/', profile_edit, name='profile edit'),
    path('details/<int:pk>', ProfileDetailsView.as_view(), name='profile details'),
    path('edit/<int:pk>', ProfileEditView.as_view(), name='profile edit'),
    path('edit-done/', ProfileEditDoneView.as_view(), name='profile edit done')
]
