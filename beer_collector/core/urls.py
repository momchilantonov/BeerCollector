from django.urls import path
from beer_collector.core.views import home_page

urlpatterns = [
    path('', home_page, name='home page')
]
