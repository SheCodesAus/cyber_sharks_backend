from django.db import models
from django.contrib.auth import get_user_model
from locations.models import Location


EXPERIENCE_LEVEL_CHOICES = [
    ("Beginner", "beginner"),
    ("Junior", "junior"),
    ("Mid", "mid"),
    ("Senior", "senior"),
]

CONTACT_METHOD_CHOICES = [
    ("Email", "email"),
    ("Phone", "phone"),
    ("LinkedIn", "linkedin"),
]


class SpecialisationChoices(models.TextChoices):
    PYTHON = "Python", "python"
    DJANGO = "Django", "django"
    REACTJS = "ReactJs", "reactjs"
    HTMLCSS = "Html/Css", "html/css"
    JAVA = "Java", "java"
    CSHARP = "Csharp", "csharp"
    JAVASCRIPT = "Javascript", "javascript"


class Specialisation(models.Model):
    name = models.CharField(
        max_length=50,
        choices=SpecialisationChoices.choices,
        default=SpecialisationChoices.PYTHON,
        unique=True,
    )

    def __str__(self):
        return self.name


class TopicChoices(models.TextChoices):
    DEVOPS = "DevOps", "devops"
    AI = "AI", "ai"
    FRONTEND = "Frontend", "frontend"
    APIDESIGN = "API design", "API Design"
    TESTING = "Testing", "testing"
    AGILEMETHODOLOGIES = "Agile methodologies", "agile methodologies"
    DATAVISUALISATION = "Data Visualisation", "data visualisation"
    RESONSIVEDESIGN = "Responsive Design", "responsive design"
    PUBLICSPEAKING = "Public Speaking", "public speaking"


class Topic(models.Model):
    name = models.CharField(max_length=50, choices=TopicChoices.choices, unique=True)

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
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    biography = models.TextField()
    # Will upload to 'products' folder in S3
    photo = models.ImageField(upload_to="portfolio/", null=True, blank=True)
    photo_url = models.URLField(max_length=200, null=True, blank=True)
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
    topics = models.ManyToManyField("Topic", related_name="portfolios", blank=True)
    occupation = models.CharField(max_length=255, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    topic_detail = models.TextField(blank=True, null=True)  
    specialisations_detail = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.first_name} {self.last_name}"
