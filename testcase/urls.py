from django.urls import path
from .views import (
    TestCaseListView,
    TestCaseCreateView,
    TestCaseUpdateView,
    TestCaseDetailView,
    TestCaseDeleteView,
)

app_name = "testcase"

urlpatterns = [
    path("", TestCaseListView.as_view(), name="index"),
    path("add/", TestCaseCreateView.as_view(), name="add"),
    path("<int:pk>/", TestCaseDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", TestCaseUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/", TestCaseDeleteView.as_view(), name="delete"),
]