from django.urls import path
from .views import UserProfileDetail, UserFollow

app_name = 'profiles'
urlpatterns = [
    path('<slug>', UserProfileDetail.as_view(), name='user-profile'),
    path('<slug>/follow', UserFollow.as_view(), name='user-follow')
]
