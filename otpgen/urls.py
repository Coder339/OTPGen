
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',include('authenticate.urls')),
    path('verify/', include('secretkey.urls')),
    path('appointment/', include('appointment.urls')),
]
