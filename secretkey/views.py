from datetime import datetime
import pyotp
import base64
import random
import string
import math
from authenticate.models import User
from django.shortcuts import render
from .models import PhoneModel,OtpModel
from .serializer import MobileSerializer,OtpSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from .serializer import OtpSerializer
from rest_framework import  generics
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from utils.permissions import IsOwnerOrReadOnly,IsSuper
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

class generateKey:
    
    @staticmethod
    def returnValue(phone):
        digits = string.digits
        length = 12
        return str(phone) + str(datetime.date(datetime.now())) + str(''.join((random.choice(digits) for i in range(length))))


class getPhoneNumberRegistered(APIView):

    authentication_classes      =   []
    permission_classes          =   [] 
    serializer_class            =   MobileSerializer

    def post(self,request,*args,**kwargs):
        print('tst')
        print(request.data.get('mobile'))
        phone = request.data['mobile']

        try:
            user = User.objects.get(contact=phone)
            print(user)
        except ObjectDoesNotExist:
            return Response({"sorry":"phone number not registered"},status=404)
        
        
       
        if PhoneModel.objects.filter(mobile=phone).exists():
             Mobile = PhoneModel.objects.get(mobile=phone)
             print('exist already')
        else:
            PhoneModel.objects.create(mobile=phone)
            Mobile = PhoneModel.objects.get(mobile=phone)
            print('newly')

        Mobile.counter += 1 # Update Counter At every Call
        Mobile.save()
        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(phone).encode())
        OTP = pyotp.HOTP(key) # HOTP Model for OTP is created
        print(OTP.at(Mobile.counter))
        otp = OTP.at(Mobile.counter)
        PhoneModel.objects.filter(mobile=phone).update(otp=otp)
    
    
        # if OtpModel.objects.filter(pk=Mobile.pk).exists():
        #     OtpModel.objects.filter(pk=Mobile.pk).update(
        #                                             mobile=phone
        #                                             )
        # else:
        #     OtpModel.objects.create(pk=Mobile.pk,mobile=phone)

        # Using Multi-Threading send the OTP Using Messaging Services like Twilio or Fast2sms
        return Response({"OTP":OTP.at(Mobile.counter)},status=200) # Just for demonstration


class VerifyOtp(generics.CreateAPIView):
    queryset                =       OtpModel.objects.all()
    serializer_class        =       OtpSerializer
    permission_classes      =       [IsAuthenticated]
    authentication_classes  =       [JSONWebTokenAuthentication,SessionAuthentication]

    def post(self,request,*args,**kwargs):
        print('otp ')
        otp = request.data['otp']
        contact=request.user.contact
        try:
            Mobile = PhoneModel.objects.get(mobile=contact)
            eotp = Mobile.otp
            print(otp)
            print(eotp)

            if str(otp) == str(eotp):
                if OtpModel.objects.filter(user=request.user).exists():
                    OtpModel.objects.filter(user=request.user).update(otp=otp)
                    response  =   {"message":"authorized","otp":otp,"status":201}
                    return Response(response,status=201)
                else:
                    self.create(request,*args,**kwargs)
                    response  =   {"message":"authorized","otp":otp,"status":201}
                    return Response(response,status=201)
            else:
                return Response({"message":"invalid OTP"})
        except:
            return Response({"message":"something wrong"})
    
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)


    # @staticmethod
    # def post(request,phone):
    #     try:
    #         Mobile = PhoneModel.objects.get(mobile=phone)

    #     except ObjectDoesNotExist:
    #         return Response("user doesn't exist",status=404)

    #     keygen = generateKey()
    #     key = base64.b32encode(keygen.returnValue(phone).encode()) # Generating Key
    #     OTP = pyotp.HOTP(key) # HOTP Model
    #     instance = OtpModel.objects.get(pk=Mobile.pk)
    #     print(instance)
    #     if (OTP.verify(instance.otp,Mobile.counter)): # Verifying the OTP
    #         Mobile.isVerified = True
    #         Mobile.save()
    #         return Response('you are authorized',status=200)
    #     return Response('OTP is Wrong',status=404)







#EXAMPLE 

# import random
# import string

# # get random string password with letters, digits, and symbols
# def get_random_password_string(length):
#     password_characters = string.ascii_letters + string.digits + string.punctuation
#     password = ''.join(random.choice(password_characters) for i in range(length))
#     print("Random string password is:", password)

# get_random_password_string(10)
# get_random_password_string(10)


#OUTPUT
# Random string password is: "C:!|]@|sh
# Random string password is: 'Q^s2q!t-N