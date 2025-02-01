import requests
from django.core.files.base import ContentFile
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Portfolio
from .serializers import PortfolioSerializer
from .permissions import IsOwnerOrReadOnly
from django.core.files.storage import default_storage


class PortfolioListCreate(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        portfolios = Portfolio.objects.all()
        serializer = PortfolioSerializer(portfolios, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        print("FILES in request:", request.FILES)  # Debug print
        print("DATA in request:", request.data)  # Debug print

        # Handle file upload if present
        # if "photo" in request.FILES:
        #     file = request.FILES["photo"]
        #     print("Received file:", file.name)  # Debug print
        #     # file_name = default_storage.save(f"portfolio/{file.name}", file)
        #     request.data["photo"] = file
        #     request.data["photo_url"] = None

        serializer = PortfolioSerializer(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            portfolio = serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print("Serializer errors:", serializer.errors)  # Debug print
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PortfolioDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            portfolio = Portfolio.objects.get(pk=pk)
            self.check_object_permissions(self.request, portfolio)
            return portfolio
        except Portfolio.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        portfolio = self.get_object(pk)
        serializer = PortfolioSerializer(portfolio, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        portfolio = self.get_object(pk)
        print("Initial request.FILES:", request.FILES)  # Debug print
        print("Initial request.data:", request.data)  # Debug print

        # if "photo" in request.FILES:
        #     file = request.FILES["photo"]
        #     # print("Processing uploaded file:", file.name)  # Debug print
        #     # file_name = default_storage.save(f"portfolio/{file.name}", file)
        #     request.data["photo"] = file
        #     request.data["photo_url"] = None

        serializer = PortfolioSerializer(
            portfolio,
            data=request.data,
            partial=True,
            context={"request": request},
        )

        if serializer.is_valid():
            print(
                "Serializer is valid, validated_data:", serializer.validated_data
            )  # Debug print
            updated_portfolio = serializer.save()
            print("After save, photo value:", updated_portfolio.photo)  # Debug print
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            print("Serializer errors:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        portfolio = self.get_object(pk)
        portfolio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
