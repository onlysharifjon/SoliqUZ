from django.db import models

# Create your models here.


class UserModel(models.Model):
    #CharField
    name = models.CharField(max_length=20)
    surename = models.CharField(max_length=20)
    password = models.CharField(max_length=32)
    PS_serial_num = models.IntegerField(unique=True)
    PS_seria = models.CharField(max_length=2)
    phone = models.IntegerField(unique=True)
    def __str__(self):
        return self.name


class Cashbacks(models.Model):
    user = models.CharField(max_length=300)
    cashback = models.IntegerField()
    def __str__(self):
        return self.user