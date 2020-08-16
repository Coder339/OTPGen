from .models import Appointment,Image
from rest_framework import serializers

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'
        read_only_fields = ['user']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields= '__all__'