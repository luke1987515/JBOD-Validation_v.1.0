from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="model_list"),
    path("add/", views.add_model, name="model_add"),
]