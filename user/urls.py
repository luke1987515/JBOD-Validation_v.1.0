from django.urls import path

from .views import UserLoginView, UserLogoutView

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView, name="logout"),
]