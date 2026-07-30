from django.contrib import admin
from django.urls import path, include

"""
全域主路由設定：統一管理專案中各子應用程式（Apps）與 Django 内建功能的 URL 網址分配。
Global Main URL Routing: Centralized URL configuration mapping paths to sub-applications and built-in features.
"""

urlpatterns = [
    # Django 後台管理介面路由 / Django Admin interface
    path("admin/", admin.site.urls),

    # 系統儀表板／首頁模組路由 / Dashboard and main landing views
    path("", include("dashboard.urls")),

    # 硬體型號管理模組路由 / Hardware model management app
    path("model/", include("models_app.urls")),

    # Django 內建身份驗證路由（登入、登出、密碼變更等） / Built-in authentication routes (login, logout, password reset)
    path("accounts/", include("django.contrib.auth.urls")),

    # 韌體管理模組路由 / Firmware management app
    path("firmware/", include("firmware.urls")),

    # 測試案例模組路由 / Test case management app
    path("testcase/", include("testcase.urls")),

    # 測試計畫模組路由 / Test plan management app
    path("testplan/", include("testplan.urls")),

    # 驗證任務執行模組路由 / Validation and execution management app
    path(
        "validation/",
        include("validation.urls"),
    ),
]