from django.urls import path
from .views import RegisterView, LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register', RegisterView.as_view(), name="register"),
    path('login', LoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name='logout'),
    # path('profile/<slug>', UserDetailView.as_view(), name="user-profile")
]
