from django.urls import path
from .views import UserProfileDetail

app_name = 'profiles'
urlpatterns = [
    path('<slug>', UserProfileDetail.as_view(), name='user-profile')
]
