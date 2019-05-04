from django.urls import path
from .views import AdventureListApi, AdventureRetrieveApi

app_name = 'travel_api'
urlpatterns = [
    path('', AdventureListApi.as_view(), name="list"),
    path('<unique_id>', AdventureRetrieveApi.as_view(), name="detail")
]
