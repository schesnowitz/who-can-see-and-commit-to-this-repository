from django.urls import path
from .views import (ProjectDetailView)
app_name = 'projects' 
urlpatterns = [
    path("<int:pk>/", ProjectDetailView.as_view(), name="project_detail"),
    # path("<int:pk>/edit/", ProjectUpdateView.as_view(), name="project_edit"),
    # path("<int:pk>/delete/", ProjectDeleteView.as_view(), name="project_delete"),
    
    # path("new/", ProjectCreateView.as_view(), name="project_new"),
]
