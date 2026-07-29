from django.contrib import admin

from .models import Validation


@admin.register(Validation)
class ValidationAdmin(admin.ModelAdmin):

    list_display = (
        "validation_id",
        "project_name",
        "model",
        "tester",
        "status",
    )

    list_filter = (
        "status",
        "model",
    )

    search_fields = (
        "validation_id",
        "serial_number",
    )