from django.db import models
from authenticate.models import User
# Create your models here.

class PhoneModel(models.Model):
    mobile     = models.IntegerField(blank=False, null=True)
    isVerified = models.BooleanField(blank=False, default=False)
    counter    = models.IntegerField(default=0, blank=False)
    otp        = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return str(self.mobile)


class OtpModel(models.Model):
    user     = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    # mobile   = models.IntegerField(blank=True, null=True)
    otp      = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return str(self.otp)