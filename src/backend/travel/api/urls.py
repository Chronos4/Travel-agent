from django.urls import path
from .views import AdventureListApi


urlpatterns=[
	path('',AdventureListApi.as_view(),name="adventure-list-api")
]