from django.urls import path

from .views import (
    TestPlanListView,
    TestPlanCreateView,
)

urlpatterns = [
    path("", TestPlanListView.as_view(), name="testplan_list"),
    path("add/", TestPlanCreateView.as_view(), name="testplan_add"),
]