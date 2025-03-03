from django.http import Http404
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .models import CustomUser
from .serializers import CustomUserSerializer, UserRegistrationSerializer
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAuthenticated,
    AllowAny,
)
from .permissions import IsOwnerOrReadOnly


class CustomUserList(APIView):
    def get_permissions(self):
        if self.request.method == "GET":
            return [IsAuthenticatedOrReadOnly()]
        elif self.request.method == "POST":
            return [AllowAny()]
        return super().get_permissions()

    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            # Add date_joined and is_active by default
            serializer.save(
                is_active=True,
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomUserDetail(APIView):
    permission_classes = [IsOwnerOrReadOnly]  # Move permission here

    def get_object(self, pk):
        try:
            obj = CustomUser.objects.get(pk=pk)
            self.check_object_permissions(self.request, obj)  # Add permission check
            return obj
        except CustomUser.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserSerializer(
            instance=user, data=request.data, partial=True, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)

        # Update last_login
        user.last_login = timezone.now()
        user.save()

        return Response(
            {
                "token": token.key,
                "user_id": user.id,
                "email": user.email,
                "is_superuser": user.is_superuser,
                "first_name": user.first_name,
                "last_name": user.last_name,
            }
        )

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(
            {"message": "Successfully logged out"}, status=status.HTTP_200_OK
        )

class UserRegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer