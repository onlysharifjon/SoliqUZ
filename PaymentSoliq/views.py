from django.shortcuts import render
from django.utils.text import slugify
# Create your views here.
import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Payment
from .serializers import PaymentSerializer, CashbacksSerializer, FiksalSeriyaSerializer
from CheckSoliq.models import Check
from drf_yasg.utils import swagger_auto_schema
from UserSoliq.models import UserModel
import datetime
import qrcode
from fpdf import FPDF
import qrcode
from .models import CardUser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from UserSoliq.models import Cashbacks
import qrcode
class PaymentVIEW(APIView):
    queryset = UserModel.objects.all()
    serializer_class = PaymentSerializer

    @swagger_auto_schema(request_body=PaymentSerializer)
    def post(self, request):
        user = request.data.get('pay_user')
        where = request.data.get('where')
        total = request.data.get('total')
        time = datetime.datetime.now()
        filter_money = CardUser.objects.all().filter(card_holder=user)
        for i in filter_money:
            if i.card_money >= total:
                email = str(i.mail_user)

                cartasidagi_pul = i.card_money - total
                saver = CardUser.objects.all().filter(card_holder=user).update(card_money=cartasidagi_pul)


                try:
                    user = UserModel.objects.all().filter(id=int(user)).first()
                except:
                    print("error excepda")
                print("ppppp")
                crea = Payment.objects.create(
                    user2=user.id, where=where, total=total, time=time).save()
                print(crea)
                list_f_id = ['UZ', 'LG', 'VG', 'NA', 'ZZ', 'EP', 'EZ']
                fiksal_id = random.choice(list_f_id)

                fiksal_belgi = ""
                for i in range(12):
                    fiksal_belgi += str(random.randint(1, 9))
                fiksal_belgi = int(fiksal_belgi)

                fiksal_seriya = ""
                for i in range(12):
                    fiksal_seriya += str(random.randint(1, 9))

                def un_random():

                    fiksal_seriya = ""
                    for i in range(12):

                        fiksal_seriya += str(random.randint(1, 9))

                if int(fiksal_seriya) in Check.objects.all().filter(fiksal_seriya=fiksal_seriya):
                    un_random()

                fiksal_seriya = int(fiksal_seriya)
                check_create = Check.objects.create(usr=int(user.id), where=where, total=total, time=time,
                                                    fiksal_seriya=fiksal_seriya, fiksal_belgi=fiksal_belgi,
                                                    fiksal_id=fiksal_id)
                check_create.save()
                # check yaratish uchun
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=12)
                pdf.cell(200, 10, txt="Fiksal ID: " + fiksal_id, ln=1, align="C")
                pdf.cell(200, 10, txt="Fiksal Belgi: " +
                                      str(fiksal_belgi), ln=1, align="C")
                pdf.cell(200, 10, txt="Fiksal Seriya: " +
                                      str(fiksal_seriya), ln=1, align="C")
                pdf.cell(200, 10, txt="User: " + str(user), ln=1, align="C")
                pdf.cell(200, 10, txt="Where: " + str(where), ln=1, align="C")
                pdf.cell(200, 10, txt="Total: " + str(total), ln=1, align="C")
                pdf.cell(200, 10, txt="Time: " + str(time), ln=1, align="C")

                # qr code yaratish uchun
                img = qrcode.make(f"http://164.92.101.201:8000/pay/cashback/{fiksal_seriya}")
                img.save(f"uploads/check{fiksal_seriya}.png")
                # save in pdf
                pdf.image(f"uploads/check{fiksal_seriya}.png", x=80 - 10, y=80, w=80)
                pdf.output(f"uploads/check{fiksal_seriya}.pdf")
                pdf_path = f"uploads/check{fiksal_seriya}.pdf"
                with open(pdf_path, 'rb') as pdf_file:
                    response = HttpResponse(pdf_file.read(), content_type='application/pdf')
                    response['Content-Disposition'] = f'attachment; filename="uploads/check{fiksal_seriya}.pdf"'
                import smtplib
                from email.mime.text import MIMEText
                from email.mime.multipart import MIMEMultipart
                #________________________________________________________________________________________
                # Email and SMTP server details
                sender_email = "mominovsharif12@gmail.com"
                receiver_email = f"{email}"
                password = "uorv tkma xoxp jpcr"
                smtp_server = "smtp.gmail.com"
                smtp_port = 587  # For Gmail, use 587 for TLS

                # Create the email content
                subject = "SOLIQ UZ"
                body = f"😐Sizning Kartangizdan Pul Yechib Olindi😐\n\n\nYechib Olingan Pul Miqdori: {total}😢"
                message = MIMEMultipart()
                message["From"] = sender_email
                message["To"] = receiver_email
                message["Subject"] = subject
                message.attach(MIMEText(body, "plain"))
                pdf_filename = f"uploads/check{fiksal_seriya}.pdf"
                with open(pdf_filename, 'rb') as pdf_file:
                    pdf_attachment = MIMEApplication(pdf_file.read(), _subtype="pdf")
                    pdf_attachment.add_header('Content-Disposition', f'attachment; filename={pdf_filename}')
                    message.attach(pdf_attachment)

                try:
                    server = smtplib.SMTP(smtp_server, smtp_port)
                    server.starttls()
                    server.login(sender_email, password)
                    server.sendmail(sender_email, "mominovsharif12@gmail.com", message.as_string())
                    print('Email sent successfully!')
                except Exception as e:
                    print(f'Error: {e}')
                finally:
                    server.quit()
                #_______________________________________________________________________________________
                return response
            else:
                return Response({"message": "Kartada Yetarli Mablag` mavjud emas"})


              
              
              
              
              
              
              
              
              
              
              
class Cashback_API_GET(APIView):


    def get(self, request, fiksal_seriya):
        # mashini boolean field bilan filter qilish kere
        cash = Check.objects.all().filter(
            fiksal_seriya=fiksal_seriya, status_check=False).first()
        if cash:
            cashback1 = cash.total / 100
            pulcha = Cashbacks.objects.all().filter(user=cash.usr).first()
            if pulcha is None:
                a = 0
                b = cashback1 + a
                saver = Cashbacks.objects.create(
                    user=cash.usr, cashback=int(b)).save()
                # create qr code
                return Response({'message': 'success'}, status=status.HTTP_200_OK)
            else:
                a = pulcha.cashback
                b = cashback1 + a
                saver = Cashbacks.objects.all().filter(user=cash.usr).update(cashback=int(b))
                return Response({'message': 'success'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'error2'}, status=status.HTTP_400_BAD_REQUEST)

# check
