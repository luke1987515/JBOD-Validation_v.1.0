from django.urls import path

from . import views

urlpatterns = [

    path("", views.index, name="firmware_list"),

    path("add/", views.add_firmware, name="firmware_add"),

    path("<int:pk>/", views.detail_firmware, name="firmware_detail"),

    path("<int:pk>/edit/", views.edit_firmware, name="firmware_edit"),

    path("<int:pk>/delete/", views.delete_firmware, name="firmware_delete"),

]