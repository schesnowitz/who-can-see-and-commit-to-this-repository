from django.urls import path
from .views import PostListView, PostDetailView, SearchResultsView, create_post_view
app_name = 'aiposts' 
urlpatterns = [
    path("new/", create_post_view, name="create_post"),
    path("posts/", PostListView.as_view(), name="post_list"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("search/", SearchResultsView.as_view(), name="search"), 
]
