from django.db import models
from django.contrib.auth import get_user_model
from locations.models import Location

# We will need to install Pillow if we want to upload actual photos - right now it is written for a file field

EXPERIENCE_LEVEL_CHOICES = [
    ("BEGINNER", "Beginner"),
    ("JUNIOR", "Junior"),
    ("MID", "Mid"),
    ("SENIOR", "Senior"),
]

CONTACT_METHOD_CHOICES = [
    ("EMAIL", "Email"),
    ("PHONE", "Phone"),
    ("LINKEDIN", "LinkedIn"),
]


class Specialisation(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ContactPreferences(models.Model):
    portfolio = models.OneToOneField(
        "Portfolio", on_delete=models.CASCADE, related_name="contact_preferences"
    )
    preferred_method = models.CharField(
        max_length=20, choices=CONTACT_METHOD_CHOICES, default="EMAIL"
    )
    additional_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Contact Preferences for {self.portfolio.user.username}"


class Portfolio(models.Model):
    id = models.AutoField(primary_key=True)
    profile_name = models.CharField(
        max_length=255
    )  # Renamed from 'biography' to 'profile_name' to match API
    biography = models.TextField()
    photo = models.URLField(
        max_length=500, blank=True, null=True
    )  # Changed to URLField
    linkedin_url = models.URLField(max_length=200, blank=True, null=True)
    email = models.EmailField(unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    experience_level = models.CharField(
        max_length=20,
        choices=EXPERIENCE_LEVEL_CHOICES,
        default="BEGINNER",
    )
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, related_name="portfolios"
    )
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="portfolios"
    )
    specialisations = models.ManyToManyField(Specialisation, related_name="portfolios")

    def __str__(self):
        return f"{self.user.username} - {self.profile_name}"
