
from django.contrib import admin
from django.urls import path
from myapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base, name='base'),
    path('productlist/',productlist, name='productlist'),
    path('productADD/',productADD, name='productADD'),
]
