from django.contrib import admin
from .models import TestPlan


@admin.register(TestPlan)
class TestPlanAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "model",
        "firmware",
        "created_at",
    )

    search_fields = (
        "name",
    )

    filter_horizontal = (
        "testcases",
    )