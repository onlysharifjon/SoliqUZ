from django.shortcuts import render

# Create your views here.
import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Payment
from .serializers import PaymentSerializer
from CheckSoliq.models import Check
from drf_yasg.utils import swagger_auto_schema
from UserSoliq.models import UserModel
import datetime
import qrcode
from fpdf import FPDF
class PaymentVIEW(APIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    @swagger_auto_schema(request_body=PaymentSerializer)
    def post(self, request):
        user = request.data.get('user')
        where = request.data.get('where')
        total = request.data.get('total')
        time = datetime.datetime.now()
        # try:
        #     user = UserModel.objects.all().filter(id=int(user))
        #     return Response({'message': 'success'}, status=status.HTTP_200_OK)
        # except:
        #     return Response({'message': 'User Not found'}, status=status.HTTP_404_NOT_FOUND)
        # print(type(user), where, total, time)
        # # return Response({'message': 'success'}, status=status.HTTP_200_OK)
        # create = Payment.objects.create(user=user, where=where, total=total, time=time)
        # list_f_id = ['UZ', 'LG', 'VG', 'NA', 'ZZ', 'EP', 'EZ']
        # fiksal_id = random.choice(list_f_id)
        #
        # fiksal_belgi = ""
        # for i in range(12):
        #     fiksal_belgi += str(random.randint(1, 9))
        # fiksal_belgi = int(fiksal_belgi)
        #
        # fiksal_seriya = ""
        # for i in range(12):
        #     fiksal_seriya += str(random.randint(1, 9))

        #
        # def un_random():
        #     fiksal_seriya = ""
        #     for i in range(12):
        #         fiksal_seriya += str(random.randint(1, 9))
        # if int(fiksal_seriya) in Check.objects.all().filter(fiksal_seriya=fiksal_seriya):
        #     un_random()

        #
        #
        # fiksal_seriya = int(fiksal_seriya)
        # check_create = Check.objects.create(user=int(user), where=where, total=total, time=time,fiksal_seriya=fiksal_seriya,
        #                                     fiksal_belgi=fiksal_belgi,fiksal_id=fiksal_id)
        # check_create.save()
        # #write pdf check
        # pdf = FPDF()
        # pdf.add_page()
        # pdf.set_font("Arial", size=12)
        # pdf.cell(200, 10, txt="Fiksal ID: "+fiksal_id, ln=1, align="C")
        # pdf.cell(200, 10, txt="Fiksal Belgi: "+str(fiksal_belgi), ln=1, align="C")
        # pdf.cell(200, 10, txt="Fiksal Seriya: "+str(fiksal_seriya), ln=1, align="C")
        # pdf.cell(200, 10, txt="User: "+str(user), ln=1, align="C")
        # pdf.cell(200, 10, txt="Where: "+str(where), ln=1, align="C")
        # pdf.cell(200, 10, txt="Total: "+str(total), ln=1, align="C")
        # pdf.cell(200, 10, txt="Time: "+str(time), ln=1, align="C")
        # pdf.output(f"uploads/check{fiksal_seriya}.pdf")
        # return Response({'message': 'success'}, status=status.HTTP_200_OK)
        #
        #

