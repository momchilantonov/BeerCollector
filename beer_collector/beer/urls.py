from django.urls import path
from beer_collector.beer.views.beer import (
    CreateBeerView, EditBeerView, DeleteBeerView, DeleteBeerDoneView,
    BeerListView, beer_like, beer_comment, BeerUserListView, BeerDetails,
)
from beer_collector.beer.views.beer_style import (
    CreateBeerStyleView, EditBeerStyleView, DeleteBeerStyleView, DeleteBeerStyleDoneView,
    BeerStyleListView, BeerStyleUserListView, beer_style_like, beer_style_comment, BeerStyleDetails,
)

urlpatterns = [
    path('beer-style-create/', CreateBeerStyleView.as_view(), name='beer style create'),
    path('beer-style-edit/<int:pk>', EditBeerStyleView.as_view(), name='beer style edit'),
    path('beer-style-delete/<int:pk>', DeleteBeerStyleView.as_view(), name='beer style delete'),
    path('beer-style-delete-done/', DeleteBeerStyleDoneView.as_view(), name='beer style delete done'),
    path('beer-style-list/', BeerStyleListView.as_view(), name='beer style list'),
    path('beer-style-user-list/', BeerStyleUserListView.as_view(), name='beer style user list'),
    path('beer-style-details/<int:pk>', BeerStyleDetails.as_view(), name='beer style details'),
    path('beer-style-like/<int:pk>', beer_style_like, name='beer style like'),
    path('beer-style-comment/<int:pk>', beer_style_comment, name='beer style comment'),
    path('beer-create/', CreateBeerView.as_view(), name='beer create'),
    path('beer-edit/<int:pk>', EditBeerView.as_view(), name='beer edit'),
    path('beer-delete/<int:pk>', DeleteBeerView.as_view(), name='beer delete'),
    path('beer-delete-done/', DeleteBeerDoneView.as_view(), name='beer delete done'),
    path('beer-list/', BeerListView.as_view(), name='beer list'),
    path('beer-user-list/', BeerUserListView.as_view(), name='beer user list'),
    path('beer-details/<int:pk>', BeerDetails.as_view(), name='beer details'),
    path('beer-like/<int:pk>', beer_like, name='beer like'),
    path('beer-comment/<int:pk>', beer_comment, name='beer comment'),
]
