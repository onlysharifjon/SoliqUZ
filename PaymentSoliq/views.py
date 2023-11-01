from django.shortcuts import render

# Create your views here.
import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Payment
from .serializers import PaymentSerializer
from CheckSoliq.models import Check

import datetime
class PaymentVIEW(APIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def post(self, request):
        user = request.data.get('user')
        where = request.data.get('where')
        total = request.data.get('total')
        time = datetime.datetime.now()
        create = Payment.objects.create(user=user, where=where, total=total, time=time)
        list_f_id = ['UZ', 'LG', 'VG', 'NA', 'ZZ', 'EP', 'EZ']
        fiksal_id = random.choice(list_f_id)
        fiksal_belgi = ""
        for i in range(12):
            fiksal_belgi+=str(random.randint(1,9))
        fiksal_belgi = int(fiksal_belgi)
        #salom


        check_create = Check.objects.create(user=user, where=where, total=total, time=time)

