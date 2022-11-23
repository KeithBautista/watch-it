from django.urls import path
from .views import UserRegistrationView, UserEditView

urlpatterns = [
    path('registration/', UserRegistrationView.as_view(), name="registration"),
    path('edit_profile/', UserEditView.as_view(), name="edit_profile"),
]
