from django.urls import path
from .views import UserRegistrationView, UserEditView, PasswordsChangeView, ProfilePageView
from django.contrib.auth import views as auth_views
from . import views
# Allows us to use authentication views from django

urlpatterns = [
    path('registration/', UserRegistrationView.as_view(), name="registration"),
    path('edit_profile/', UserEditView.as_view(), name="edit_profile"),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),
    path('password_success/', views.password_success, name="password_success"),
    path('<int:pk>/profile/', ProfilePageView.as_view(), name="profile-page"),



]
