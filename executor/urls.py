from django.urls import path

from . import views

app_name = "executor"

urlpatterns = [

    # Execute Home
    path(
        "",
        views.index,
        name="index",
    ),

    # Stop Execute Job
    path(
        "<int:pk>/stop/",
        views.stop_job,
        name="stop",
    ),

]