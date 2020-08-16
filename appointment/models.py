from django.db import models
from authenticate.models import User
# Create your models here.

class Appointment(models.Model):
    user          = models.ForeignKey(User,on_delete=models.CASCADE,null=True,editable=False)
    name          = models.CharField(max_length=50,blank=False,null=True)
    address       = models.CharField(max_length=50,blank=False,null=True)
    phone         = models.IntegerField(blank=False,null=True)
    # date          = models.DateField()
    # time          = models.TimeField()
    img           = models.ImageField(upload_to='static/images',null=True)

    def __str__(self):
        return self.name



class Image(models.Model):
    # property_id = models.ForeignKey(Appointment,on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to='static/images')