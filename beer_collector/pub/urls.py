from django.urls import path
from beer_collector.pub.views import CreatePubView, EditPubView, DeletePubView, DeletePubDoneView, PubListView

urlpatterns = [
    path('pub-create/', CreatePubView.as_view(), name='pub create'),
    path('pub-edit/<int:pk>', EditPubView.as_view(), name='pub edit'),
    path('pub-delete/<int:pk>', DeletePubView.as_view(), name='pub delete'),
    path('pub-delete-done/', DeletePubDoneView.as_view(), name='pub delete done'),
    path('pub-list/', PubListView.as_view(), name='pub list'),

]
