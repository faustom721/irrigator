from rest_framework import serializers

from .models import Schedule
from .models import PlantationField


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ("field", "weekdays", "hours_start", "durations")
        read_only_fields = ("field",)


class PlantationFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantationField
        fields = "__all__"
