from django.urls import path
from .views import ListDestinationView, DetailDestinationView


urlpatterns = [
    path('', ListDestinationView.as_view(), name='destination-list'),
    path('<unique_id>', DetailDestinationView.as_view(), name="destination-detail")
]
