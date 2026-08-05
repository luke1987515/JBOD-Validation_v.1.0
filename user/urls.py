from django.urls import path

from .views import UserLoginView
from .views import UserLogoutView
from .views import register

urlpatterns = [

    path(
        "login/",
        UserLoginView.as_view(),
        name="login",
    ),

    path(
        "register/",
        register,
        name="register",
    ),

    path(
        "logout/",
        UserLogoutView,
        name="logout",
    ),

]