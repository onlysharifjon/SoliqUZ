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


class Register(APIView):
    serializer_class = ForLoginSerializer

    @swagger_auto_schema(request_body=ForLoginSerializer)
    def post(self, request):
        serializer = ForLoginSerializer(data=request.data)
        seriya = request.data.get('PS_seria')
        seriya_num = request.data.get('PS_serial_num')
        print(type(seriya_num))
        password = request.data.get('password')
        phone = request.data.get('phone')
        name = request.data.get('name')
        surename = request.data.get('surename')
        user = UserModel.objects.filter(PS_seria=seriya, PS_serial_num=seriya_num, password=password).first()
        acsess_token = AccessToken.for_user(user)
        if serializer.is_valid():

            serializer.save()
            return Response({"Register Success": acsess_token})