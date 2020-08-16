
from django.shortcuts import render,redirect
from django.views import generic
from django.urls import reverse_lazy
from authenticate.models import *
# from secretkey.models import OtpModel
from .serializer import LoginSerializer,RegisterSerializer
from django.contrib.auth import authenticate,login,get_user_model
# from rest_framework.authentication import SessionAuthentication
from rest_framework import permissions,authentication
from rest_framework import generics,mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import (
    generics,
    status,
)
from utils.permissions import *
# from django.core.exceptions import ObjectDoesNotExist
# from .serializer import OtpSerializer
# from datetime import datetime
# import pyotp
# import base64
# import random
# import string
# import math



# User = get_user_model()

class RegistrationView(generics.CreateAPIView):
    authentication_classes      =   []
    permission_classes          =   [] 
    serializer_class            =   RegisterSerializer
    # queryset                    =   User.objects.all()

    

    def post(self,request,*args,**kwargs):
        if request.method == 'POST':
            serializer = RegisterSerializer(data = request.data)
            data = {}
            if serializer.is_valid():
                user = serializer.save()
                data['response'] = RegisterSerializer.get_message(self,obj=user)
                data['email']    = user.email
                data['username'] = user.username
                data['token']    = RegisterSerializer.get_token(self,obj=user)  # token generation view @
            else:
                data = serializer.errors
            
            return Response(data)



# User=get_user_model()


class LoginAPIView(generics.GenericAPIView):
    authentication_classes      =   []
    permission_classes          =   []
    serializer_class            =   LoginSerializer
    # queryset                    =   User.objects.all()


    def post(self,request):
        username            =   request.data.get('username')
        password            =   request.data.get('password')
        user                =   authenticate(username=username,password=password)
        data = {}
        print(username)
        print(password)
        print(user)
        print(request.data)
        if user is not None:
            print('vvvv')
            login(request,user)
            serializer = LoginSerializer(data = request.data)
            data['response'] = LoginSerializer.get_message(self,obj=user)
            # response    =   {'messages':'you are logged in ...'}
            data['token']    = LoginSerializer.get_token(self,obj=user)
            # return Response(response)
            return Response(data)

        response    =   {'messages':'invalid credentials'}
        return Response(response)



# class generateKey:
    
#     @staticmethod
#     def returnValue(phone):
#         digits = string.digits
#         length = 12
#         return str(phone) + str(datetime.date(datetime.now())) + str(''.join((random.choice(digits) for i in range(length))))


# class getOtpView(generics.CreateAPIView):

    
#     def post(self,request,*args,**kwargs):

#         try:
#             user = User.objects.get(contact__iexact=request.data['mobile'])
#             if user.exists():
#                 self.create(request,*args,**kwargs)
#             # response  =   {"message":"authorized","status":201}
#             # return Response(response,status=201) 
#             user.counter += 1 # Update Counter At every Call
#             user.save()
#             print(user.pk)
#             keygen = generateKey()
#             key = base64.b32encode(keygen.returnValue(request.data['mobile']).encode())
#             OTP = pyotp.HOTP(key) # HOTP Model for OTP is created
#             print(OTP.at(user.counter))
#             otp = OTP.at(user.counter)
        
#             if OtpModel.objects.filter(pk=Mobile.pk).exists():
#                 OtpModel.objects.filter(pk=Mobile.pk).update(
#                                                         mobile=phone
#                                                         )
#             else:
#                 OtpModel.objects.create(pk=Mobile.pk,mobile=phone)

#             # Using Multi-Threading send the OTP Using Messaging Services like Twilio or Fast2sms
#             return Response({"OTP":OTP.at(Mobile.counter)},status=200) # Just for demonstration

#         except ObjectDoesNotExist:   
#             return Response({'messages':'mobile number not provided'})

        