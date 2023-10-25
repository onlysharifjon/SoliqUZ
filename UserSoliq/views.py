from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ForLoginSerializer
# Create your views here.
from .models import UserModel


class LoginUserSoliq(APIView):
    queryset = UserModel.objects.all()
    serializer_class = ForLoginSerializer

    def post(self, request):
        seriya = request.data.get('PS_seria')
        seriya_num = request.data.get('PS_serial_num')
        password = request.data.get('password')
        if UserModel.objects.all().filter(PS_seria=seriya, PS_serial_num=seriya_num, password=password).exists():
            user = UserModel.objects.get(PS_seria=seriya, PS_serial_num=seriya_num, password=password)
            return Response({"user": self.serializer_class(user).data})


