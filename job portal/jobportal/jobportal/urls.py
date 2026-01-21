
from django.contrib import admin
from django.urls import path,include
from jobportalapp.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('jobportalapp.urls')),
    
]
