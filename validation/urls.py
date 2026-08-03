"""
validation/urls.py
"""

from django.urls import path

from . import views

app_name = "validation"

urlpatterns = [

    # Validation List
    path(
        "",
        views.validation_list,
        name="index",
    ),

    # Add Validation
    path(
        "add/",
        views.add_validation,
        name="add",
    ),

    # Validation Detail
    path(
        "<int:pk>/",
        views.detail_validation,
        name="detail",
    ),

    # Edit Validation
    path(
        "<int:pk>/edit/",
        views.edit_validation,
        name="edit",
    ),

    # Delete Validation
    path(
        "<int:pk>/delete/",
        views.delete_validation,
        name="delete",
    ),

]