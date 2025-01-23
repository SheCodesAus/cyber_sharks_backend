from django.shortcuts import render
from rest_framework import generics, filters, serializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from users.models import CustomUser
from portfolio.models import Portfolio, Specialisation
from locations.models import Location
from users.serializers import CustomUserSerializer
from portfolio.serializers import PortfolioSerializer, SpecialisationSerializer
from locations.serializers import LocationSerializer
from rest_framework.pagination import PageNumberPagination

VALID_SEARCH = [
    "user", 
    "portfolio", 
    "location", 
    "specialisation"
    ]

# This is to limit the ammount of data returned - will make load time better etc in case heaps returns
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class SearchView(generics.ListAPIView):
    """
    A search view to filter data across Users, Portfolios, Locations, and Specialisations.
    """

    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = []  # fields are dynamically set in the view logic!!!
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        query_type = self.request.query_params.get(
            "type", "portfolio")  # deffault to Portfolio
        if query_type not in VALID_SEARCH:
            raise serializers.ValidationError({"detail": f"Sorry, you can't search for, {query_type}"})
        search_query = self.request.query_params.get("search", "")

        if query_type == "user":
            return CustomUser.objects.filter(username__icontains=search_query)
        elif query_type == "location":
            return Location.objects.filter(name__icontains=search_query)
        elif query_type == "specialisation":
            specialisations = search_query.split(
                ","
            )  # allows to search multiples eg python, django
            return Portfolio.objects.filter(
                specialisations__name__icontains=search_query
            ).distinct()  # distnct to avoid duplicate results if multiple matches
        else:
            return Portfolio.objects.filter(profile_name__icontains=search_query)

    def get_serializer_class(self):
        query_type = self.request.query_params.get("type", "portfolio")
        if query_type == "user":
            return CustomUserSerializer
        elif query_type == "location":
            return LocationSerializer
        elif query_type == "specialisation":
            return PortfolioSerializer
        else:
            return PortfolioSerializer
