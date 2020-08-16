from django.urls import path, include
from .views import (
    AppointmentCreateAPIView,
    AppointmentDetailAPIView,
    AppointmentEditAPIView,
    AppointmentListAPIView,
    ImageView)

urlpatterns = [
    path('create/',AppointmentCreateAPIView.as_view()),
    path('detail/',AppointmentDetailAPIView.as_view()),
    path('update/<pk>/',AppointmentEditAPIView.as_view()),
    path('list/',AppointmentListAPIView.as_view()),
    path('image/',ImageView.as_view())
    
]