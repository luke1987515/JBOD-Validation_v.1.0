"""
validation/urls.py
"""

from django.urls import path

from . import views

urlpatterns = [

    path(
        "",
        views.validation_list,
        name="validation_list",
    ),

    path(
        "add/",
        views.add_validation,
        name="validation_add",
    ),

    path(
        "<int:pk>/",
        views.detail_validation,
        name="validation_detail",
    ),

    path(
        "<int:pk>/edit/",
        views.edit_validation,
        name="validation_edit",
    ),

    path(
        "<int:pk>/delete/",
        views.delete_validation,
        name="validation_delete",
    ),

]