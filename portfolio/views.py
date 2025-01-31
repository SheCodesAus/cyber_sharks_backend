
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
        # Handle file upload if present
        if 'file' in request.FILES:
            file = request.FILES['file']
            file_name = default_storage.save(f"portfolio/{file.name}", file)
            request.data['photo'] = file
            request.data['photo_url'] = None

        serializer = PortfolioSerializer(
            data=request.data, 
            context={"request": request}
        )
        if serializer.is_valid():
            portfolio = serializer.save(user=request.user)
            image_url = request.data.get('image_url')
            if image_url:
                response = requests.get(image_url)
                if response.status_code == 200:
                    file_name = image_url.split("/")[-1]
                    portfolio.photo.save(file_name, ContentFile(response.content), save=False)
                    portfolio.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
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
        

        if 'photo' in request.FILES:
            file = request.FILES['photo']
            file_name = default_storage.save(f"portfolio/{file.name}", file)
            request.data['photo'] = file
            request.data['photo_url'] = None


        serializer = PortfolioSerializer(
            portfolio,
            data=request.data,
            partial=True,
            context={"request": request},
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            print("Serializer errors:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        portfolio = self.get_object(pk)
        portfolio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)