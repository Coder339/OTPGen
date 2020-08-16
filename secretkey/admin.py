from django.contrib import admin
from .models import PhoneModel,OtpModel
# Register your models here.
admin.site.register(PhoneModel)
admin.site.register(OtpModel)