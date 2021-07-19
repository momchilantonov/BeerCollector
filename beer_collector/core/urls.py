from django.urls import path
from beer_collector.core.views import index

urlpatterns = [
    path('', index, name='home page')
]
