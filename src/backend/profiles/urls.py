from django.urls import path
from .views import UserProfileDetail


urlpatterns = [
    path('<slug>', UserProfileDetail.as_view(), name='user-profile')
]
