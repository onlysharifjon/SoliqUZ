from django.contrib import admin
from .models import Payment
from UserSoliq.models import Cashbacks, UserModel
from CheckSoliq.models import Check
from PaymentSoliq.models import CardUser

admin.site.register(Payment)
admin.site.register(Cashbacks)
admin.site.register(Check)
admin.site.register(CardUser)


# Register your models here.
