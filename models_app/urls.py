from django.urls import path

from . import views

urlpatterns = [

    path("", views.index, name="model_list"),

    path("add/", views.add_model, name="model_add"),

    path("<int:pk>/", views.detail_model, name="model_detail"),

    path("<int:pk>/edit/", views.edit_model, name="model_edit"),

    path("<int:pk>/delete/", views.delete_model, name="model_delete"),

]