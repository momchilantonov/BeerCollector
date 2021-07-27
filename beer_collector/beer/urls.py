from django.urls import path
from beer_collector.beer.views import (
    create_beer_style, edit_beer_style, delete_beer_style,
    beer_style_details, create_beer, edit_beer, delete_beer, beer_details
)

urlpatterns = [
    path('create-beer-style/', create_beer_style, name='create beer style'),
    path('edit-beer-style/<int:pk>', edit_beer_style, name='edit beer style'),
    path('delete-beer-style/<int:pk>', delete_beer_style, name='delete beer style'),
    path('beer-style-details/<int:pk>', beer_style_details, name='beer style details'),
    path('create-beer/', create_beer, name='create beer'),
    path('edit-beer/<int:pk>', edit_beer, name='edit beer'),
    path('delete-beer/<int:pk>', delete_beer, name='delete beer'),
    path('beer-details/<int:pk>', beer_details, name='beer details'),
]
