from django.contrib import admin
from .models import JBODModel


@admin.register(JBODModel)
class JBODModelAdmin(admin.ModelAdmin):

    list_display = (
        "model_name",
        "vendor",
        "platform",
        "status",
        "updated_at",
    )

    search_fields = (
        "model_name",
        "vendor",
    )

    list_filter = (
        "vendor",
        "status",
    )

    ordering = (
        "model_name",
    )