from django.db import migrations


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

SPECIALISATION_CHOICES = [
    ("Python", "python"),
    ("Django", "django"),
    ("ReactJs", "reactjs"),
    ("Html/Css", "html/css"),
    ("Java", "java"),
    ("Csharp", "csharp"),
    ("Javascript", "javascript"),
]

TOPIC_CHOICES = [
    ("DevOps", "devops"),
    ("AI", "ai"),
    ("Frontend", "frontend"),
    ("API design", "API Design"),
    ("Testing", "testing"),
    ("Agile methodologies", "agile methodologies"),
    ("Data Visualisation", "data visualisation"),
    ("Responsive Design", "responsive design"),
    ("Public Speaking", "public speaking"),
]


def populate_choices(apps, schema_editor):
    Specialisation = apps.get_model("portfolio", "Specialisation")
    Topic = apps.get_model("portfolio", "Topic")
    ContactPreferences = apps.get_model("portfolio", "ContactPreferences")

    # Ensure Specialisation choices exist
    for name, value in SPECIALISATION_CHOICES:
        Specialisation.objects.get_or_create(name=value)

    # Ensure Topic choices exist
    for name, value in TOPIC_CHOICES:
        Topic.objects.get_or_create(name=value)

    # Ensure ContactPreferences choices exist
    for obj in ContactPreferences.objects.all():
        if obj.preferred_method not in [choice[1] for choice in CONTACT_METHOD_CHOICES]:
            obj.preferred_method = "email"  # Set to a default valid choice
            obj.save()

    # Ensure Portfolio experience levels exist
    Portfolio = apps.get_model("portfolio", "Portfolio")
    for obj in Portfolio.objects.all():
        if obj.experience_level not in [
            choice[1] for choice in EXPERIENCE_LEVEL_CHOICES
        ]:
            obj.experience_level = "beginner"  # Set to a default valid choice
            obj.save()


def remove_choices(apps, schema_editor):
    Specialisation = apps.get_model("portfolio", "Specialisation")
    Topic = apps.get_model("portfolio", "Topic")

    # Remove only the choices that were inserted by this migration
    Specialisation.objects.filter(
        name__in=[value for _, value in SPECIALISATION_CHOICES]
    ).delete()
    Topic.objects.filter(name__in=[value for _, value in TOPIC_CHOICES]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0010_alter_contactpreferences_preferred_method_and_more"),
    ]

    operations = [
        migrations.RunPython(populate_choices, reverse_code=remove_choices),
    ]
