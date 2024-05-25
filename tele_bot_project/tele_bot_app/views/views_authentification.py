
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework import viewsets, filters, generics, status
from ..models.models_registration import Registration
from rest_framework.views import APIView
from rest_framework.response import Response


#Authentification
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=False)
        username = serializer.validated_data['username']
        token, created = Token.objects.get_or_create(username=username)
        return Response({'token': token.key})


class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if email and password:
            username = Registration.objects.filter(email=email).first()
            if username and username.email == email and username.password == password:  # user and user.check_password(password):
                #token, created = Token.objects.get_or_create(username=username)
                response_data = {
                    'message': 'Вы зашли в свой личный кабинет!'
                }
                return Response(response_data, status=status.HTTP_200_OK) # {'token': token.key}
            return Response({'error': 'Неверные учетные данные'}, status=status.HTTP_400_BAD_REQUEST)