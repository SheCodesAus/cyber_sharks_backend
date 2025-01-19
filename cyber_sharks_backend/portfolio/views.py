# portfolio/views.py

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.http import Http404
from .models import Portfolio
from .serializers import PortfolioSerializer
from .permissions import IsOwnerOrReadOnly


# portfolio/views.py

class PortfolioList(APIView):
    """
    List all portfolios or create a new portfolio.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        portfolios = Portfolio.objects.all()
        serializer = PortfolioSerializer(portfolios, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = PortfolioSerializer(data=request.data)
        if serializer.is_valid():
            # Automatically associate the portfolio with the authenticated user
            serializer.save(user=request.user) # relies on portfolio model having user FK make sure naming is correct when lucy updates users app
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# portfolio/views.py

class PortfolioDetail(APIView):
    """
    Retrieve, update, or delete a portfolio instance.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_object(self, pk):
        """
        Helper method to get the object with given pk.
        """
        try:
            portfolio = Portfolio.objects.get(pk=pk)
            self.check_object_permissions(self.request, portfolio)
            return portfolio
        except Portfolio.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        portfolio = self.get_object(pk)
        serializer = PortfolioSerializer(portfolio)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        portfolio = self.get_object(pk)
        serializer = PortfolioSerializer(portfolio, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        portfolio = self.get_object(pk)
        portfolio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
