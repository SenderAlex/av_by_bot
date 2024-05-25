
from django.urls import path, include
from ..views.views_authentification import CustomAuthToken, LoginView


urlpatterns = [
    path('auth/', include('rest_framework.urls')),  # осуществляет log out в API???????
    #path('api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth'),
    path('api/login/', LoginView.as_view(), name='login'),
]
