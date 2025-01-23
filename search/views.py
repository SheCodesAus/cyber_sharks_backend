from django.shortcuts import render
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from users.models import CustomUser  # Replace with your actual user model
from portfolio.models import Portfolio
from locations.models import Location
from users.serializers import UserSerializer  # Replace with your actual user serializer
from portfolio.serializers import PortfolioSerializer
from locations.serializers import LocationSerializer

class SearchView(generics.ListAPIView):
    """
    A generic search view to filter data across Users, Portfolios, and Locations.
    """
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'description']  

    def get_queryset(self):
        query_type = self.request.query_params.get('type', 'portfolio')  
        search_query = self.request.query_params.get('search', '')  

        if query_type == 'user':  
            return CustomUser.objects.filter(username__icontains=search_query)
        elif query_type == 'location':  
            return Location.objects.filter(name__icontains=search_query)
        else:  
            return Portfolio.objects.filter(name__icontains=search_query)

    def get_serializer_class(self):
        query_type = self.request.query_params.get('type', 'portfolio')
        if query_type == 'user':
            return UserSerializer
        elif query_type == 'location':
            return LocationSerializer
        else:
            return PortfolioSerializer
