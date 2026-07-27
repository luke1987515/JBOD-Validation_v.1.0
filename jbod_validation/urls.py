from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", include("dashboard.urls")),

    path("model/", include("models_app.urls")),

    path("accounts/", include("django.contrib.auth.urls")),

    path("firmware/", include("firmware.urls")),

    path("testcase/", include("testcase.urls")),

    path("testplan/", include("testplan.urls")),
]