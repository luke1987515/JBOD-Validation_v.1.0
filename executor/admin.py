from django.contrib import admin

from .models import ExecuteJob
from .models import ExecuteLog


@admin.register(ExecuteJob)
class ExecuteJobAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "testplan",
        "status",
        "progress",
        "created_at",
    )


@admin.register(ExecuteLog)
class ExecuteLogAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "job",
        "level",
        "message",
        "created_at",
    )

    list_filter = (
        "level",
    )

    search_fields = (
        "message",
    )