
from django.contrib import admin
from django.urls import path
from myapp.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',studentAdd,name='studentAdd'),
    # path('studentDelete',studentDelete,name='studentDelete'),
    # path('studentEdit',studentEdit,name='studentEdit'),
    path('',base,name='base'),
    path('studentlist/',studentlist,name='studentlist'),
]
