from django.contrib import admin
from .models import TestCase


@admin.register(TestCase)
class TestCaseAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "timeout",
        "status",
        "created_at",
    )

    list_filter = (
        "category",
        "status",
    )

    search_fields = (
        "name",
        "command",
    )