from django.contrib import admin
from .models import Payment
from UserSoliq.models import Cashbacks, UserModel
from CheckSoliq.models import Check

admin.site.register(Payment)
admin.site.register(Cashbacks)
admin.site.register(Check)


# Register your models here.
