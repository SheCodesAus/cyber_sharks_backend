# portfolio/serializers.py

from rest_framework import serializers

from locations.models import CityChoice
from .models import Portfolio, Specialisation, ContactPreferences, Location
from locations.serializers import LocationSerializer
from users.serializers import CustomUserSerializer


class SpecialisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialisation
        fields = ["id", "name"]


class ContactPreferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactPreferences
        fields = ["preferred_method", "additional_info"]


class PortfolioSerializer(serializers.ModelSerializer):
    location = serializers.ChoiceField(choices=CityChoice.choices)
    photo = serializers.URLField(required=False, allow_blank=True, allow_null=True)
    user = CustomUserSerializer(read_only=True)
    specialisations = serializers.PrimaryKeyRelatedField(
        queryset=Specialisation.objects.all(), many=True
    )
    contact_preferences = ContactPreferencesSerializer(required=False, allow_null=True)
    email = serializers.EmailField()
    linkedin_url = serializers.URLField(
        required=False, allow_blank=True, allow_null=True
    )

    class Meta:
        model = Portfolio
        fields = [
            "id",
            "profile_name",
            "biography",
            "photo",
            "linkedin_url",
            "email",
            "created_date",
            "experience_level",
            "location",
            "specialisations",
            "contact_preferences",
            "user",
        ]
        read_only_fields = ["id", "created_date", "user"]

    def create(self, validated_data):
        location_name = validated_data.pop("location")
        specialisations_data = validated_data.pop("specialisations", [])
        contact_preferences_data = validated_data.pop("contact_preferences", None)

        location, created = Location.objects.get_or_create(city_name=location_name)
        portfolio = Portfolio.objects.create(
            location=location, user=self.context["request"].user, **validated_data
        )
        portfolio.specialisations.set(specialisations_data)

        if contact_preferences_data:
            ContactPreferences.objects.create(
                portfolio=portfolio, **contact_preferences_data
            )

        return portfolio

    def update(self, instance, validated_data):
        location_name = validated_data.pop("location", None)
        specialisations_data = validated_data.pop("specialisations", None)
        contact_preferences_data = validated_data.pop("contact_preferences", None)

        if location_name:
            location, created = Location.objects.get_or_create(city_name=location_name)
            instance.location = location

        if specialisations_data is not None:
            instance.specialisations.set(specialisations_data)

        if contact_preferences_data:
            contact_pref, created = ContactPreferences.objects.get_or_create(
                portfolio=instance
            )
            for attr, value in contact_preferences_data.items():
                setattr(contact_pref, attr, value)
            contact_pref.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance
