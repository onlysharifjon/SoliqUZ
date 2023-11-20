from enum import auto

from django.db import models
from UserSoliq.models import UserModel


class Check(models.Model):
    # user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    usr = models.CharField(max_length=200)
    where = models.CharField(max_length=255)
    total = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)
    CHOISES = (
        ('UZ', 'UZ'),
        ('LG', 'LG'),
        ('VG', 'VG'),
        ('NA', 'NA'),
        ('ZZ', 'ZZ'),
        ('EP', 'EP'),
        ('EZ', 'EZ'),
    )
    fiksal_id = models.CharField(max_length=2, choices=CHOISES)
    fiksal_belgi = models.IntegerField()
    fiksal_seriya = models.IntegerField()
    # mashini bollean filed qilish kere
    status_check = models.BooleanField(default=False)
    def __str__(self):
        return self.user
