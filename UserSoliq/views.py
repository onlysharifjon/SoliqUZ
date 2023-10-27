from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .serializers import ForLoginSerializer
from .models import UserModel
from drf_yasg.utils import swagger_auto_schema

class LoginUserSoliq(APIView):
    serializer_class = ForLoginSerializer

    @swagger_auto_schema(request_body=ForLoginSerializer)
    def post(self, request):
        seriya = request.data.get('PS_seria')
        seriya_num = request.data.get('PS_serial_num')
        password = request.data.get('password')

        print(f"Credentials: seriya={seriya}, seriya_num={seriya_num}, password={password}")

        if seriya and seriya_num and password:
            # Authenticate the user
            user = authenticate(request, PS_seria=seriya, PS_serial_num=seriya_num, password=password)
            print(f"User: {user}")

            if user is not None:
                # If authentication is successful, generate an access token
                refresh = RefreshToken.for_user(user)

                return Response({
                    "user": self.serializer_class(user).data,
                    'Acsess_Token': str(refresh.access_token),
                })

        # If authentication fails or missing credentials, return an error response
        return Response("Invalid credentials", status=status.HTTP_401_UNAUTHORIZED)
