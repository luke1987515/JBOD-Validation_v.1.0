from django.contrib import admin
from .models import TestCase


@admin.register(TestCase)
class TestCaseAdmin(admin.ModelAdmin):

    list_display = (
        "case_id",
        "name",
        "category",
        "timeout",
        "status",
    )

    list_filter = (
        "category",
        "status",
    )

    search_fields = (
        "case_id",
        "name",
    )

    ordering = (
        "case_id",
    )