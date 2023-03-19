from dataclasses import field
from django.db import models


class Estate(models.Model):
    """The real estate property"""

    name = models.CharField(max_length=150)
    user = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="estates"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Estates"
        unique_together = (
            "user",
            "name",
        )

    def __str__(self):
        return self.name


class WaterSupply(models.Model):
    """Water supply for the field. Could be a tank with a pump or connected to the water network of the property."""

    name = models.CharField(max_length=150)
    estate = models.ForeignKey(
        "Estate", on_delete=models.CASCADE, related_name="water_supplies"
    )
    supply_type = models.CharField(
        max_length=10, choices=[("tank", "tank"), ("network", "network")]
    )

    class Meta:
        verbose_name_plural = "Water supplies"

    def __str__(self):
        return self.name


class FieldPlantation(models.Model):
    """
    The field of a plantation. For example a field of tomatoes. This represents fisically the plantation,
    if the user has more than one tomatoes plantations fisically separated, it should create more FieldPlantations
    """

    name = models.CharField(max_length=150)
    water_supply = models.ForeignKey(
        WaterSupply, on_delete=models.DO_NOTHING, related_name="field_plantations"
    )
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

    # class Meta:

    #     models.UniqueConstraint(
    #         fields=["field_plantation", "is_active"], name="unique_field_active"
    #     ),

    def __str__(self):
        return self.name


class Schedule(models.Model):
    """When a FieldPlantation gets watered"""

    name = models.CharField(max_length=150, null=True, blank=True)
    is_active = models.BooleanField(
        default=False
    )  # A FieldPlantation can have multiple Schedules, but only one can be active at a time.
    # The rest would be just for archive and reuse purposes. # This is constrainted below.
    field_plantation = models.ForeignKey(
        FieldPlantation, on_delete=models.CASCADE, related_name="schedules"
    )

    # These three fields are used to define the field's irrigation schedule
    weekdays = models.JSONField(
        default=[False, False, False, False, False, False, False]
    )  # which days. Mark True for the day slot you want to water
    hours_start = models.JSONField(
        default=[[], [], [], [], [], [], []]
    )  # at what hour. For each weekday slot, put the hour you want to water in 24h format
    durations = models.JSONField(
        default=[[0], [0], [0], [0], [0], [0], [0]]
    )  # for how long. For each weekday slot, put the duration in minutes you want to water
    humidity_blocker = models.BooleanField(
        default=False
    )  # if true, the irrigation of the day won't start if the humidity is above humidity_blocker_value%
    humidity_blocker_value = models.IntegerField(
        default=80
    )  # the humidity value that will trigger the humidity blocker

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["field_plantation", "is_active"], name="unique_field_active"
            ),
            models.UniqueConstraint(
                fields=["field_plantation", "name"], name="unique_field_name"
            ),
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
