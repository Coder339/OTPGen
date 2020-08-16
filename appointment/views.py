from django.shortcuts import render
from .models import Appointment,Image
from rest_framework.parsers import JSONParser,MultiPartParser,FormParser
from rest_framework.authentication import SessionAuthentication
from .serializer import AppointmentSerializer,ImageSerializer
from rest_framework import  generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from utils.permissions import IsOwnerOrReadOnly,IsSuper
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class AppointmentCreateAPIView(generics.CreateAPIView):
    parser_classes          =       (MultiPartParser, FormParser)
    queryset                =       Appointment.objects.all()
    serializer_class        =       AppointmentSerializer
    permission_classes      =       []
    authentication_classes  =       []

    def post(self,request,*args,**kwargs):
        print(request.user)
        try:
            self.create(request,*args,**kwargs)
            response  =   {"message":"created","status":201}
            return Response(response,status=201)
        except:
            return Response({"message":"your form is invalid and duplication not allowed"})

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)




class AppointmentEditAPIView(generics.UpdateAPIView):
    queryset                =       Appointment.objects.all()
    serializer_class        =       AppointmentSerializer
    permission_classes      =       []
    authentication_classes  =       []
    lookup_field            =       'user'


class AppointmentListAPIView(generics.ListAPIView):
    queryset                =       Appointment.objects.all()
    serializer_class        =       AppointmentSerializer
    permission_classes      =       []
    authentication_classes  =       []



class AppointmentDetailAPIView(generics.GenericAPIView):
    queryset                =       Appointment.objects.all()
    serializer_class        =       AppointmentSerializer
    permission_classes      =       []
    authentication_classes  =       []


    def get(self,request,*args,**kwargs):
        request             =       self.request
        user                =       request.user
        qs                  =       Appointment.objects.get(user=user)
        serialize           =       AppointmentSerializer(qs)
        return Response(serialize.data)



class ImageView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request):
        all_images = Image.objects.all()
        serializer = ImageSerializer(all_images, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):

        # converts querydict to original dict
        images = dict((request.data).lists())['image']
        flag = 1
        arr = []
        for img_name in images:
            modified_data = modify_input_for_multiple_files(
                                                            img_name
                                                            )
            file_serializer = ImageSerializer(data=modified_data)
            if file_serializer.is_valid():
                file_serializer.save()
                arr.append(file_serializer.data)
            else:
                flag = 0

        if flag == 1:
            return Response(arr, status=status.HTTP_201_CREATED)
        else:
            return Response(arr, status=status.HTTP_400_BAD_REQUEST)


def modify_input_for_multiple_files(image):
    dict = {}
    dict['image'] = image
    return dict