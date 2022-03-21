from dataclasses import field
from django.db import models


class Schedule(models.Model):
    field = models.ForeignKey("plants.Field", on_delete=models.CASCADE)

    # these three fields are used to define the field's irrigation schedule
    weekdays = models.JSONField(
        default=[False, False, False, False, False, False, False]
    )
    hours_start = models.JSONField(default=[[], [], [], [], [], [], []])
    durations = models.JSONField(default=[[0], [0], [0], [0], [0], [0], [0]])

    def __str__(self):
        return str(self.weekdays)
