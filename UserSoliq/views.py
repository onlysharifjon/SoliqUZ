from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.contrib.auth import authenticate
from .serializers import ForLoginSerializer
from .models import UserModel
from drf_yasg.utils import swagger_auto_schema
import jwt


class LoginUserSoliq(APIView):
    serializer_class = ForLoginSerializer

    @swagger_auto_schema(request_body=ForLoginSerializer)
    def post(self, request):
        seriya = request.data.get('PS_seria')
        seriya_num = request.data.get('PS_serial_num')
        password = request.data.get('password')
        # return jwt token
        # user = authenticate(UserModel.objects.filter(PS_seria=seriya, PS_serial_num=seriya_num, password=password).first())
        user = UserModel.objects.filter(PS_seria=seriya, PS_serial_num=seriya_num, password=password).first()
        return Response({"Login Success": user.id})


from rest_framework.response import Response
from rest_framework import status

class Register(APIView):
    serializer_class = ForLoginSerializer

    @swagger_auto_schema(request_body=ForLoginSerializer)
    def post(self, request):
        serializer = ForLoginSerializer(data=request.data)
        if serializer.is_valid():
            seriya = request.data.get('PS_seria')
            seriya_num = request.data.get('PS_serial_num')
            password = request.data.get('password')
            phone = request.data.get('phone')
            name = request.data.get('name')
            surename = request.data.get('surename')
            crt = UserModel.objects.create(phone=phone, name=name, surename=surename, password=password,
                                           PS_serial_num=seriya_num, PS_seria=seriya)
            user = UserModel.objects.filter(PS_seria=seriya, PS_serial_num=seriya_num, password=password).first()
            if user:
                acsess_token = AccessToken.for_user(user)
                # serializer.save()  # Save the serializer after creating the user
                return Response({"Register Success": str(acsess_token)})
            else:
                return Response({"error": "User not found with provided credentials"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#