from django.urls import path
from .views import FirmwareListView, FirmwareCreateView

urlpatterns = [
    path("", FirmwareListView.as_view(), name="firmware_list"),
    path("add/", FirmwareCreateView.as_view(), name="firmware_add"),
]