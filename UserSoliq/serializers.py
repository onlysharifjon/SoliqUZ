from rest_framework import serializers
from .models import UserModel


class ForLoginSerializer(serializers.Serializer):
    class Meta:
        model = UserModel
        fields = ['PS_serial_num','PS_seria','password']