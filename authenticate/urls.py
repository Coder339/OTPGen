from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token
from . import views

urlpatterns = [
    # JWT
    path('jwt/',obtain_jwt_token),
    path('jwt/refresh/',refresh_jwt_token),
    
    path('register/',views.RegistrationView.as_view(),name = 'register'),
    path('login/',views.LoginAPIView.as_view()),
]