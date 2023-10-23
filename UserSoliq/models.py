from django.db import models

# Create your models here.


class UserModel(models.Model):
    #CharField
    name = models.CharField(max_length=20)
    surename = models.CharField(max_length=20)
    password = models.CharField(max_length=32)
    PS_serial_num = models.IntegerField(max_length=7,unique=True)
    PS_seria = models.CharField(max_length=2)
    phone = models.IntegerField(max_length=9,unique=True)


    def __str__(self):
        return self.name
