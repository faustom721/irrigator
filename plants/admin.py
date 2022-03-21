from django.contrib import admin

from .models import *


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ("name", "user")
    search_fields = ["name", "user__username"]


@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ("name", "property", "user")
    search_fields = ["name", "user__username", "property__name"]

    def user(self, obj):
        return obj.property.user
