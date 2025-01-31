from rest_framework import serializers
from locations.models import CityChoice
from .models import Portfolio, Specialisation, ContactPreferences, Location, Topic
from locations.serializers import LocationSerializer
from users.serializers import CustomUserSerializer
import requests
from django.core.files.base import ContentFile

class SpecialisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialisation
        fields = ["id", "name"]

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ["id", "name"]

class ContactPreferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactPreferences
        fields = ["preferred_method", "additional_info"]

class PortfolioSerializer(serializers.ModelSerializer):
    location = serializers.ChoiceField(choices=CityChoice.choices)
    photo = serializers.ImageField(required=False, allow_null=True)
    photo_url = serializers.URLField(required=False, allow_null=True)
    user = CustomUserSerializer(read_only=True)
    
    specialisations = serializers.SlugRelatedField(
        many=True, 
        slug_field="name", 
        queryset=Specialisation.objects.all()
    )

    topics = serializers.SlugRelatedField(
        many=True,
        slug_field="name",
        queryset=Topic.objects.all(),
        required=False,
    )

    contact_preferences = ContactPreferencesSerializer(required=False, allow_null=True)
    email = serializers.EmailField()
    linkedin_url = serializers.URLField(required=False, allow_blank=True, allow_null=True)

    class Meta:
        model = Portfolio
        fields = [
            "id", "first_name", "last_name", "biography", "photo", "photo_url",
            "linkedin_url", "email", "created_date", "experience_level",
            "location", "specialisations", "topics", "contact_preferences",
            "user", "occupation", "company", "topic_detail", "specialisations_detail",
        ]
        read_only_fields = ["id", "created_date", "user"]

    def validate(self, attrs):
        # First run the existing validation
        attrs = super().validate(attrs)
        
        # Check if both photo and photo_url are provided
        if 'photo' in attrs and 'photo_url' in attrs and attrs['photo'] and attrs['photo_url']:
            raise serializers.ValidationError(
                "Please provide either a photo file or a photo URL, not both."
            )
        
        return attrs

    def create(self, validated_data):
        location_name = validated_data.pop("location")
        specialisations_data = validated_data.pop("specialisations", [])
        topics_data = validated_data.pop("topics", [])
        contact_preferences_data = validated_data.pop("contact_preferences", None)
        
        # Clear the other photo field based on what was provided
        if validated_data.get('photo_url'):
            validated_data['photo'] = None
        elif validated_data.get('photo'):
            validated_data['photo_url'] = None

        # Create the location and portfolio
        location, created = Location.objects.get_or_create(city_name=location_name)
        portfolio = Portfolio.objects.create(location=location, **validated_data)

        # Set many-to-many relationships
        portfolio.specialisations.set(specialisations_data)
        portfolio.topics.set(topics_data)

        # Create contact preferences if provided
        if contact_preferences_data:
            ContactPreferences.objects.create(
                portfolio=portfolio, 
                **contact_preferences_data
            )

        return portfolio

    def update(self, instance, validated_data):
        location_name = validated_data.pop("location", None)
        specialisations_data = validated_data.pop("specialisations", None)
        topics_data = validated_data.pop("topics", None)
        contact_preferences_data = validated_data.pop("contact_preferences", None)

        # Handle photo fields
        if 'photo_url' in validated_data:
            instance.photo = None
            instance.photo_url = validated_data.pop('photo_url')
        elif 'photo' in validated_data:
            instance.photo_url = None
            instance.photo = validated_data.pop('photo')

        # Update location if provided
        if location_name:
            location, created = Location.objects.get_or_create(city_name=location_name)
            instance.location = location

        # Update many-to-many relationships if provided
        if specialisations_data is not None:
            instance.specialisations.set(specialisations_data)
        if topics_data is not None:
            instance.topics.set(topics_data)

        # Update contact preferences if provided
        if contact_preferences_data:
            contact_pref, created = ContactPreferences.objects.get_or_create(
                portfolio=instance
            )
            for attr, value in contact_preferences_data.items():
                setattr(contact_pref, attr, value)
            contact_pref.save()

        # Update remaining fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance