
from ..serializers.serializers_registration import RegistrationSerializer
from rest_framework import viewsets, filters, generics, status
from ..models.models_registration import Registration
from rest_framework.views import APIView
from rest_framework.response import Response


#Registration
class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        username = serializer.initial_data['username']
        email = serializer.initial_data['email']

        if serializer.is_valid():
            serializer.save()
            response_data = {
                'message': 'Вы успешно зарегистрированы!'
            }
            return Response({**serializer.data, **response_data}, status=status.HTTP_201_CREATED)
        elif Registration.objects.get(username=username).username == username and Registration.objects.get(username=username).email == email:
            response_error = {
                'error': 'Пользователь с таким именем или почтовым ящиком уже зарегистрирован'
            }
            return Response(response_error, status=status.HTTP_409_CONFLICT)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


