from django.db import models
# Create your models here.
from UserSoliq.models import UserModel


class Payment(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    where = models.CharField(max_length=255)
    total = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user
