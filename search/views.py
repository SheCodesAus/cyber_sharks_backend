
from portfolio.models import Portfolio, Specialisation
from locations.models import Location
from portfolio.serializers import PortfolioSerializer
from rest_framework.exceptions import ValidationError
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from locations.models import CityChoice 

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
        location = self.request.query_params.get("location", None)
        # topics = self.request.query_params.getlist("topic", [])  # Multi-select for topics
        specialisations = self.request.query_params.getlist("specialisation", [])  # Multi-select for specialisations

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

        # # Filter by topics (if implemented by someone else later)
        # if topics:
        #     queryset = queryset.filter(topics__name__in=topics).distinct()
        #     if not queryset.exists():
        #         raise ValidationError(
        #             {
        #                 "topics": f"Oops! We couldn't find any users specializing in the topics: {', '.join(topics)}."
        #             }
        #         )

        # Validate and filter by specialisations
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

        # Final validation for empty results
        if not queryset.exists():
            filters = []
            if location:
                filters.append(f"location '{location}'")
            # if topics:
            #     filters.append(f"topics {', '.join(topics)}")
            if specialisations:
                filters.append(f"specialisations {', '.join(specialisations)}")
            raise ValidationError(
                {
                    "detail": f"Oops! We couldn't find any Prism users matching: {', '.join(filters)}."
                }
            )

        return queryset

    def get_serializer_class(self):
        """
        Use the PortfolioSerializer for all responses since the main data is about Portfolios.
        """
        return PortfolioSerializer
