from dataclasses import field
from django.db import models


class Schedule(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    field = models.ForeignKey("plants.Field", on_delete=models.CASCADE)

    # these three fields are used to define the field's irrigation schedule
    weekdays = models.JSONField(
        default=[False, False, False, False, False, False, False]
    )
    hours_start = models.JSONField(default=[[], [], [], [], [], [], []])
    durations = models.JSONField(default=[[0], [0], [0], [0], [0], [0], [0]])

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["field", "is_active"], name="unique_field_active"
            ),
            models.UniqueConstraint(fields=["field", "name"], name="unique_field_name"),
        ]

    def display_weekdays(self):
        def iconize(enabled):
            if enabled:
                return "✅"
            else:
                return "❌"

        return f"Monday: {iconize(self.weekdays[0])} |\
            Tuesday: {iconize(self.weekdays[1])} |\
            Wednesday: {iconize(self.weekdays[2])} |\
            Thursday: {iconize(self.weekdays[3])} |\
            Friday: {iconize(self.weekdays[4])} |\
            Saturday: {iconize(self.weekdays[5])} |\
            Sunday: {iconize(self.weekdays[6])}"

    def __str__(self):
        return self.name
