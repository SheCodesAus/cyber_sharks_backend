# portfolio/admin.py

from django.contrib import admin
from .models import Portfolio, Specialisation, Topic, ContactPreferences


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "first_name",
        "last_name",
        "email",
        "experience_level",
        "created_date",
    )
    search_fields = ("user__username", "email", "first_name", "last_name" "biography")
    list_filter = ("experience_level", "created_date", "location")
    ordering = ("-created_date",)


@admin.register(Specialisation)
class SpecialisationAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(ContactPreferences)
class ContactPreferencesAdmin(admin.ModelAdmin):
    list_display = ("portfolio", "preferred_method")
    search_fields = ("portfolio__user__username", "preferred_method")
