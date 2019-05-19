from django.urls import path
from .views import ListDestinationView, DetailDestinationView, AdventureJoin, DeleteDestinationView

app_name = 'travel'

urlpatterns = [
    path('', ListDestinationView.as_view(), name='destination-list'),
    path('<unique_id>', DetailDestinationView.as_view(), name="destination-detail"),
    path('<unique_id>/join', AdventureJoin, name="adventure-join"),
    path('<unique_id>/delete', DeleteDestinationView.as_view(),
         name="destination-delete"),
]
