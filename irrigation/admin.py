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


@admin.register(PlantationField)
class PlantationFieldAdmin(admin.ModelAdmin):
    list_display = ("name", "water_supply", "is_planted")
    search_fields = ["field__estate__name", "name", "identification"]


@admin.register(WaterSupply)
class WaterSupplyAdmin(admin.ModelAdmin):
    list_display = ("name", "estate", "supply_type")
    search_fields = ["name", "estate__name", "supply_type"]
