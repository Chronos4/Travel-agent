from django.urls import path
from .views import UserProfileDetail, UserFollow, CreateProfile, photo_upload_view

app_name = 'profiles'
urlpatterns = [
    path('<slug>/creation', CreateProfile.as_view(), name='create-profile'),
    path('<slug>', UserProfileDetail.as_view(), name='user-profile'),
    path('<slug>/follow', UserFollow.as_view(), name='user-follow'),
    path('<slug>/upload', photo_upload_view, name="photo-upload"),
]
