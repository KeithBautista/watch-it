from django.urls import path
from .views import UserRegistrationView

urlpatterns = [
    path('registration/', UserRegistrationView.as_view(), name="registration"),
]
