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

    # Execute Detail
    path(
        "<int:pk>/",
        views.detail,
        name="detail",
    ),

    # Stop Execute Job
    path(
        "<int:pk>/stop/",
        views.stop_job,
        name="stop",
    ),

    path(
    "<int:pk>/start/",
    views.start_job,
    name="start",
),

]