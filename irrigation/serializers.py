from rest_framework import serializers

from .models import Schedule
from .models import Field


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ("field", "weekdays", "hours_start", "durations")
        read_only_fields = ("field",)


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = "__all__"
