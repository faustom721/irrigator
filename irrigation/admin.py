from django.contrib import admin

from .models import *


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ("name", "field", "property", "display_weekdays", "is_active")
    search_fields = ["name", "field", "field", "field__property__name"]

    def property(self, obj):
        return obj.field.property
