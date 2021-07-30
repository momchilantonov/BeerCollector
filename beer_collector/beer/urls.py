from django.urls import path
from beer_collector.beer.views.beer_style import (
    CreateBeerStyleView, EditBeerStyleView, BeerStyleListView,
    beer_style_details, beer_style_like, beer_style_comment,
)

urlpatterns = [
    path('create-beer-style/', CreateBeerStyleView.as_view(), name='create beer style'),
    path('edit-beer-style/<int:pk>', EditBeerStyleView.as_view(), name='edit beer style'),
    path('beer-style-list/', BeerStyleListView.as_view(), name='beer style list'),
    path('beer-style-list/<int:pk>', beer_style_details, name='beer style details'),
    path('beer_style_like/<int:pk>', beer_style_like, name='beer style like'),
    path('beer_style_add_comment/<int:pk>', beer_style_comment, name='beer style add comment'),
]
