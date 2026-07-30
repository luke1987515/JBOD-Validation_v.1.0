from django.urls import path

from . import views

"""
JBOD 機型模組路由設定：對應 JBOD 機型（JBODModel）相關頁面與 CRUD 功能的 URL 網址路徑。
JBOD Model URL Routing: Maps URL paths to corresponding views for JBODModel CRUD operations.
"""

urlpatterns = [
    # 機型列表首頁 / JBOD model list view
    path("", views.index, name="model_list"),

    # 新增機型頁面 / Add new JBOD model view
    path("add/", views.add_model, name="model_add"),

    # 檢視特定機型詳細資訊 (根據 Primary Key) / Detail view for a specific JBOD model by PK
    path("<int:pk>/", views.detail_model, name="model_detail"),

    # 編輯特定機型資料 (根據 Primary Key) / Edit view for a specific JBOD model by PK
    path("<int:pk>/edit/", views.edit_model, name="model_edit"),

    # 刪除特定機型資料 (根據 Primary Key) / Delete view for a specific JBOD model by PK
    path("<int:pk>/delete/", views.delete_model, name="model_delete"),
]