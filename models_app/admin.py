from django.contrib import admin
from .models import JBODModel


@admin.register(JBODModel)
class JBODModelAdmin(admin.ModelAdmin):
    """
    JBOD 型號管理介面設定：用於在 Django 後台管理 JBOD 硬體型號資料庫記錄。
    JBODModel Admin Configuration: Controls the admin interface for managing JBOD hardware model records.
    """

    # 後台列表頁面顯示的欄位 / Fields to display in the admin list view
    list_display = (
        "model_name",
        "vendor",
        "platform",
        "status",
        "updated_at",
    )

    # 關鍵字搜尋欄位（支援型號名稱、供應商） / Fields searchable via the search bar
    search_fields = (
        "model_name",
        "vendor",
    )

    # 側邊欄過濾條件（可依供應商、狀態進行篩選） / Sidebar filters (filter by vendor and status)
    list_filter = (
        "vendor",
        "status",
    )

    # 預設排序規則：按型號名稱升冪排序 / Default ordering: Ascending by model name
    ordering = (
        "model_name",
    )