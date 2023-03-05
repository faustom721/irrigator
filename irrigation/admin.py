from django.contrib import admin

from .models import *


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "field_plantation",
        "estate",
        "display_weekdays",
        "is_active",
    )
    search_fields = ["name", "field_plantation", "field__property__name"]

    def estate(self, obj):
        return obj.field.estate
