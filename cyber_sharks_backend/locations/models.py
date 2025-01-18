# Hardcoded locations for now - should we have this so it is user input and they can enter their own location

from django.db import models

class Location(models.Model):
    class CityChoice(models.TextChoices):
        BRISBANE = "Brisbane", "Brisbane"
        SYDNEY = "Sydney", "Sydney"
        PERTH = "Perth", "Perth"
        MELBOURNE = "Melbourne", "Melbourne"
        ADELAIDE = "Adelaide", "Adelaide"
        DARWIN = "Darwin", "Darwin"
        CANBERRA = "Canberra", "Canberra"
        GOLD_COAST = "Gold Coast", "Gold Coast"

    name = models.CharField(
        max_length=50,
        choices=CityChoice.choices,
        default=CityChoice.BRISBANE,
        unique=True,
    )

    def __str__(self):
        return self.name
