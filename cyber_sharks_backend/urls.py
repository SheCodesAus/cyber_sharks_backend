"""
URL configuration for cyber_sharks_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from users.views import CustomAuthToken

urlpatterns = [
    path("admin/", admin.site.urls),
    # Users App URLs
    path("", include("users.urls")),  # Existing users URLs at root
    # Portfolio App URLs
    path("portfolios/", include("portfolio.urls")),  # New portfolio URLs
    # Authentication
    path("api-token-auth/", CustomAuthToken.as_view(), name="api_token_auth"),
    # Search App URLs
    path("search/", include("search.urls")),
]
