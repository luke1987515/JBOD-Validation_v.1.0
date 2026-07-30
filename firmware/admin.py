from django.contrib import admin
from .models import Firmware


@admin.register(Firmware)
class FirmwareAdmin(admin.ModelAdmin):
    """
    韌體模型管理介面設定：用於在 Django 後台管理 Firmware 資料庫記錄。
    Firmware Admin Configuration: Controls the admin interface for managing Firmware database records.
    """

    # 後台列表頁面顯示的欄位 / Fields to display in the admin list view
    list_display = (
        "firmware_type",
        "version",
        "vendor",
        "build_number",
        "release_date",
        "status",
    )

    # 側邊欄過濾條件（可依韌體類型、狀態進行篩選） / Sidebar filters (filter by firmware type and status)
    list_filter = (
        "firmware_type",
        "status",
    )

    # 關鍵字搜尋欄位（支援版本號、廠商、Build 號碼） / Fields searchable via the search bar
    search_fields = (
        "version",
        "vendor",
        "build_number",
    )

    # 預設排序規則：先按韌體類型升冪排序，再按發布日期降冪排序（最新發布在前）
    # Default ordering: Ascending by firmware type, then descending by release date (newest first)
    ordering = (
        "firmware_type",
        "-release_date",
    )