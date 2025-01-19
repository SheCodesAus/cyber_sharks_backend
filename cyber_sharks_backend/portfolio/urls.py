# portfolio/urls.py

from django.urls import path
from .views import Portfolio, PortfolioDetail

urlpatterns = [
    path("", Portfolio.as_view(), name="portfolio"),  # Handles /portfolios/
    path(
        "<int:pk>/", PortfolioDetail.as_view(), name="portfolio-detail"
    ),  # Handles /portfolios/<id>/
]
