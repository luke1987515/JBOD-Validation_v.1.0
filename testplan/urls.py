from django.urls import path

from .views import (
    TestPlanListView,
    TestPlanCreateView,
)

app_name = "testplan"

urlpatterns = [
    path("", TestPlanListView.as_view(), name="index"),
    path("add/", TestPlanCreateView.as_view(), name="add"),
]