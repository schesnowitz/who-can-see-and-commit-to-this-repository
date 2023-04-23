from django.urls import path
from .views import SignUpView, EditView
from django.contrib.auth.views import PasswordChangeView
# app_name = 'account'
urlpatterns = [
    # path("signup/", SignUpView.as_view(), name="signup"),
    
    path("edit/", EditView.as_view(), name="edit"),
]