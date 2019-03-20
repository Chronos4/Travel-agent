from django.urls import path
from .views import ListDestinationView


urlpatterns = [
    path('', ListDestinationView.as_view(), name='destination-list')
]
