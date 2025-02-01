from portfolio.models import Portfolio, Specialisation
from locations.models import Location
from portfolio.serializers import PortfolioSerializer
from rest_framework.exceptions import ValidationError
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from locations.models import CityChoice
from django.db.models import Q
from rest_framework.response import Response


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class SearchView(generics.ListAPIView):
    filter_backends = []
    pagination_class = StandardResultsSetPagination

    def get(self, request, *args, **kwargs):
        # Extract query parameters
        location = request.query_params.get("location")
        topics = [
            t.lower() for t in request.query_params.get("topic", "").split(",") if t
        ]  # Convert to lowercase
        specialisations = [
            s.lower()
            for s in request.query_params.get("specialisation", "").split(",")
            if s
        ]  # Convert to lowercase

        filters = Q()

        # Validate location
        if location:
            if location.lower() not in map(
                str.lower, CityChoice.values
            ):  # Case-insensitive check
                raise ValidationError(
                    {
                        "location": f"Woah. Where is {location}? That's not on our system, are you sure it exists?"
                    }
                )
            filters &= Q(location__city_name=location)  # Case-insensitive filtering

        # Validate and filter by specialisations
        if specialisations:
            valid_specialisations = set(
                Specialisation.objects.filter(name__in=specialisations).values_list(
                    "name", flat=True
                )
            )
            invalid_specialisations = set(specialisations) - {
                s.lower() for s in valid_specialisations
            }

            if invalid_specialisations:
                raise ValidationError(
                    {
                        "specialisations": f"Oops! This tech stack doesn't exist?: {', '.join(invalid_specialisations)}"
                    }
                )

            filters &= Q(
                specialisations__name__in=valid_specialisations
            )  # Case-insensitive filtering

        # Filter by topics if provided
        if topics:
            filters &= Q(topics__name__in=topics)  # Case-insensitive filtering

        # Apply filters
        queryset = Portfolio.objects.filter(filters)

        if not queryset.exists():
            filter_details = ", ".join(
                [
                    f"{key} '{value}'"
                    for key, value in request.query_params.items()
                    if value
                ]
            )
            raise ValidationError(
                {
                    "detail": f"Oops! We couldn't find any Prism users matching: {filter_details}."
                }
            )

        return Response(
            {
                "profiles": list(
                    queryset.values(
                        "id",
                        "first_name",
                        "last_name",
                        "location__city_name",
                        "specialisations__name",
                        "topics__name",
                    ).distinct("id")
                )
            }
        )

        # return Response(queryset.values())

    def get_serializer_class(self):
        """
        Use the PortfolioSerializer for all responses since the main data is about Portfolios.
        """
        return PortfolioSerializer
