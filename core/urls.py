
from .import settings
from django.contrib.staticfiles.urls import static
from django.contrib import admin
from django.urls import path, include
from projects.views import ProjectListView, contactView
from accounts.views import EditView
urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/edit/", EditView.as_view(), name="edit"),
    path('accounts/', include('allauth.urls')),
    path("", ProjectListView.as_view(), name="project_list"),
    path("projects/", include("projects.urls")),
    path("aiposts/", include("aiposts.urls")),
    path("contact/", contactView, name="contact"),
    # path("success/", successView, name="success"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
