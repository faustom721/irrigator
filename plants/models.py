from django.db import models


class Property(models.Model):
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


class Field(models.Model):
    name = models.CharField(max_length=150)  # what is the user planting here
    property = models.ForeignKey("Property", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (
            "property",
            "name",
        )

    def __str__(self):
        return self.name
