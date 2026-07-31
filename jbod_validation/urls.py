from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # Login / Logout
    path("", include("user.urls")),

    # Dashboard
    path("", include("dashboard.urls")),

    # Model
    path("model/", include("models_app.urls")),

    # 保留 Django 內建 Authentication
    path("accounts/", include("django.contrib.auth.urls")),

    # Firmware
    path("firmware/", include("firmware.urls")),

    # TestCase
    path("testcase/", include("testcase.urls")),

    # TestPlan
    path("testplan/", include("testplan.urls")),

    # Validation
    path("validation/", include("validation.urls")),
]