from django.urls import path
from .views import UserRegistrationView, UserEditView, PasswordsChangeView, ProfilePageView, EditProfilePageView, CreateProfilePageView
from django.contrib.auth import views as auth_views
from . import views
# Allows us to use authentication views from django

urlpatterns = [
    path('registration/', UserRegistrationView.as_view(), name="registration"),
    path('edit_profile/', UserEditView.as_view(), name="edit_profile"),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),
    path('password_success/', views.password_success, name="password_success"),
    path('<int:pk>/profile/', ProfilePageView.as_view(), name="profile-page"),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name="edit-profile-page"),
    path('create_profile_page/', CreateProfilePageView.as_view(), name="create-profile-page"),
]
