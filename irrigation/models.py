from dataclasses import field
from django.db import models


class Estate(models.Model):
    name = models.CharField(max_length=150)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Properties"
        unique_together = (
            "user",
            "name",
        )

    def __str__(self):
        return self.name


class WaterSupply(models.Model):
    name = models.CharField(max_length=150)
    estate = models.ForeignKey("Estate", on_delete=models.CASCADE)
    supply_type = models.CharField(
        max_length=4, choices=[("tank", "tank"), ("network", "network")]
    )


class FieldPlantation(models.Model):
    name = models.CharField(max_length=150)
    water_supply = models.ForeignKey("WaterSupply", on_delete=models.DO_NOTHING)
    planting_date = models.DateField(null=True, blank=True)
    harvest_date = models.DateField(null=True, blank=True)
    harvest_signs = models.TextField(
        null=True, blank=True
    )  # Sometimes a field doesn't have a harvest date, but it does have a harvest signs \
    # like "When plant is 15cm tall", or "When leaves are yellow".
    is_planted = models.BooleanField(
        default=True
    )  # If false we just archive the field, for when the user plants it again. \
    # After harvest for example this becomes false.
    identification = models.CharField(
        max_length=150, null=True, blank=True
    )  # Just for identification matching, if the user has numbered/colored plantpots or something like that.
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (
            "property",
            "name",
        )

    def __str__(self):
        return self.name


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
