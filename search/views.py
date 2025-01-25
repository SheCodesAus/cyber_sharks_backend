from portfolio.models import Portfolio, Specialisation
from locations.models import Location
from portfolio.serializers import PortfolioSerializer
from rest_framework.exceptions import ValidationError
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from locations.models import CityChoice  # Import your CityChoice enum


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class SearchView(generics.ListAPIView):
    filter_backends = []
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        """
        Filter results based on selected dropdown values and validate each input.
        """
        # Extract query parameters
        location = self.request.query_params.get("city_names", None)
        specialisations = self.request.query_params.getlist("name", [])

        # Validate location against CityChoice
        if location:
            if location not in CityChoice.values:
                raise ValidationError(
                    {
                        "location": f"Woah. Where is {location}? That's not on our system, are you sure it exists?"
                    }
                )

        # Start with all Portfolios
        queryset = Portfolio.objects.all()

        # Filter by location
        if location:
            queryset = queryset.filter(location__city_name=location)
            if not queryset.exists():
                raise ValidationError(
                    {
                        "location": f"Oh no, Prism users haven't moved to {location} yet. Keep checking back!"
                    }
                )

        # Validate specialisations
        if specialisations:
            valid_specialisations = Specialisation.objects.filter(
                name__in=specialisations
            ).values_list("name", flat=True)
            invalid_specialisations = set(specialisations) - set(valid_specialisations)
            if invalid_specialisations:
                raise ValidationError(
                    {
                        "specialisations": f"Oops! This tech stack doesn't exist?: {', '.join(invalid_specialisations)}"
                    }
                )
            queryset = queryset.filter(
                specialisations__name__in=specialisations
            ).distinct()

        if not queryset.exists():
            raise ValidationError(
                {
                    "detail": f"Oops! We couldn't find any Prism users in {location} with the tech stack of {', '.join(specialisations)}."
                }
            )

        return queryset

    def get_serializer_class(self):
        """
        Use the PortfolioSerializer for all responses since the main data is about Portfolios.
        """
        return PortfolioSerializer
