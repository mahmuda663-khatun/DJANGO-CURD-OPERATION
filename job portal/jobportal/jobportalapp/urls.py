from django.contrib import admin
from django.urls import path
from jobportalapp.views import*

urlpatterns = [
    path('',signup,name='signup'),
    path('home/', home,name='home'),
    path('signin/', signin,name='signin'),
    path('signout/', signout,name='signout'),
    
]