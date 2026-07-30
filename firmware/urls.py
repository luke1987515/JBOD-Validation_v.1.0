from django.urls import path

from . import views

"""
韌體管理模組路由設定：對應韌體（Firmware）相關頁面與 CRUD 功能的 URL 網址路徑。
Firmware Module URL Routing: Maps URL paths to corresponding views for Firmware CRUD operations.
"""

urlpatterns = [
    # 韌體列表首頁 / Firmware list view
    path("", views.index, name="firmware_list"),

    # 新增韌體頁面 / Add new firmware view
    path("add/", views.add_firmware, name="firmware_add"),

    # 檢視特定韌體詳細資訊 (根據 Primary Key) / Detail view for a specific firmware by PK
    path("<int:pk>/", views.detail_firmware, name="firmware_detail"),

    # 編輯特定韌體資料 (根據 Primary Key) / Edit view for a specific firmware by PK
    path("<int:pk>/edit/", views.edit_firmware, name="firmware_edit"),

    # 刪除特定韌體資料 (根據 Primary Key) / Delete view for a specific firmware by PK
    path("<int:pk>/delete/", views.delete_firmware, name="firmware_delete"),
]