from django.urls import path
from .views import TestCaseListView, TestCaseCreateView

urlpatterns = [
    path("", TestCaseListView.as_view(), name="testcase_list"),
    path("add/", TestCaseCreateView.as_view(), name="testcase_add"),
]