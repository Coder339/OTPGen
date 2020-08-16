from .models import OtpModel,PhoneModel
from rest_framework import serializers



class MobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneModel
        fields = '__all__'
        
class OtpSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtpModel
        fields = '__all__'
        read_only_fields = ['user']

