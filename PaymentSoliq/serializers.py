from rest_framework import serializers
from .models import Payment
from UserSoliq.models import Cashbacks


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('pay_user', 'where', 'total')


class CashbacksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cashbacks
        fields = ('user', 'cashback')


from CheckSoliq.models import Check


class FiksalSeriyaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Check
        fields = ('fiksal_seriya',)
