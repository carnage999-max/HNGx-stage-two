from django.db import models


class Person(models.Model):
    name = models.CharField(
        max_length=256,
        unique=True,
        )
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

