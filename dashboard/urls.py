from django.urls import path
from . import views

print("目前載入的 views.py：", views.__file__)

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
]