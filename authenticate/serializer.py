from rest_framework import serializers
from authenticate.models import *
from django.contrib.auth import authenticate,login,get_user_model
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from utils.payload import jwt_response_payload_handler

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

# User = get_user_model()
                                                    ########### register an user
class RegisterSerializer(serializers.ModelSerializer):
    password         = serializers.CharField(style={'input_type':'password'},max_length=120,min_length=8,write_only=True)
    confirm_password = serializers.CharField(style={'input_type':'password'},max_length=120,min_length=8,write_only=True)
    token            = serializers.SerializerMethodField(read_only = True)
    message          = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = User
        fields = ['username',
                  'email',
                  'contact',
                  'password',
                  'confirm_password',
                  'token',
                  'message']

        # extra_kwargs = {
        #     'password':{'write_only':True}
        # }
    

    def get_message(self,obj):
        return 'successfully registered'

    def get_token(self,obj):
        user = obj
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        print(token)
        return token


    def create(self,validated_data):       
        user = User(
            email = self.validated_data['email'],
            username = self.validated_data['username'],
            contact = self.validated_data['contact']
        )
        password = self.validated_data['password'],
        confirm_password = self.validated_data['confirm_password'],
        
        if password != confirm_password:
            raise serializers.ValidationError({'password':'password must match'})
        user.set_password(validated_data['password'])
        user.is_active = True
        user.save()
        return user



  

    

class LoginSerializer(serializers.ModelSerializer):

    username    = serializers.CharField(max_length=120)
    password    = serializers.CharField(style={'input_type':'password'},write_only=True)
    token       = serializers.SerializerMethodField(read_only = True)
    message     = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = User
        fields = ['username',
                  'password',
                  'token',
                  'message']

        # extra_kwargs = {
        #     'password':{'write_only':True}
        # }
    
    def get_message(self,obj):
        return 'successfully logged in'

    def get_token(self,obj):
        user = obj
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        print(token)
        return token


# class OTPSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['contact']