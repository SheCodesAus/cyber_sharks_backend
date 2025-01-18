from django.urls import path
from .import views 
# from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('projects/', views.ProjectList.as_view()),
    path('projects/<int:pk>/',views.ProjectDetail.as_view()),
    # path('projects/<int:project_pk>/updates/', views.UpdateList.as_view()),
    path('pledges/', views.PledgeList.as_view()),
    path('pledges/<int:pk>/', views.PledgeDetail.as_view()),
    path('projects/<int:project_pk>/pledges/', views.ProjectPledgeList.as_view(), name='project-pledges'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)