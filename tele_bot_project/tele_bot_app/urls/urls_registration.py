
from django.urls import path, include
from ..views.views_registration import RegistrationView

urlpatterns = [
    path('api/car_registration/', RegistrationView.as_view(), name='user_registration'),
]
