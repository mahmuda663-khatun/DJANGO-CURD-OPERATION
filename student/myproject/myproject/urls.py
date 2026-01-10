
from django.contrib import admin
from django.urls import path
from myapp.views import*
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('studentList/',studentList,name='studentList'),
    path('studentADD/',studentADD,name='studentADD'),
    path('studentUpdate/',studentUpdate,name='studentUpdate'),
    path('studentDelete/',studentDelete,name='studentDelete'),
]
