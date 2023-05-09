from django.urls import path
from .views import PostListView, PostDetailView, SearchResultsView
app_name = 'aiposts' 
urlpatterns = [
    path("posts/", PostListView.as_view(), name="post_list"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("search/", SearchResultsView.as_view(), name="search"), 
]
