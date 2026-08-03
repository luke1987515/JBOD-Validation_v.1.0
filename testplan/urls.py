from django.urls import path

from .views import (
    TestPlanListView,
    TestPlanCreateView,
    TestPlanDetailView,
    TestPlanUpdateView,
)

app_name = "testplan"

urlpatterns = [

    # Test Plan List
    path(
        "",
        TestPlanListView.as_view(),
        name="index",
    ),

    # Add Test Plan
    path(
        "add/",
        TestPlanCreateView.as_view(),
        name="add",
    ),

    # Test Plan Detail
    path(
        "<int:pk>/",
        TestPlanDetailView.as_view(),
        name="detail",
    ),

    # Edit Test Plan
    path(
        "<int:pk>/edit/",
        TestPlanUpdateView.as_view(),
        name="edit",
    ),

]