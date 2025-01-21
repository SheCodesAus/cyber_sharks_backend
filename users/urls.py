from django.urls import path
from . import views

urlpatterns = [
    path('users/login/', views.CustomAuthToken.as_view()),  
    path('users/logout/', views.LogoutView.as_view()),
    path('users/<int:pk>/', views.CustomUserDetail.as_view()),
    path('users/', views.CustomUserList.as_view()),
]