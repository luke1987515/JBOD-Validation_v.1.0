from django.contrib import admin
from .models import Firmware


@admin.register(Firmware)
class FirmwareAdmin(admin.ModelAdmin):

    list_display = (
        "firmware_type",
        "version",
        "vendor",
        "build_number",
        "release_date",
        "status",
    )

    list_filter = (
        "firmware_type",
        "status",
    )

    search_fields = (
        "version",
        "vendor",
        "build_number",
    )

    ordering = (
        "firmware_type",
        "-release_date",
    )