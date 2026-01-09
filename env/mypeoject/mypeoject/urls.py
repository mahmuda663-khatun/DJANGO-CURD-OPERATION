
from django.contrib import admin
from django.urls import path
from myapp.views import studentAdd , studentDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',studentAdd,name='studentAdd'),
    path('studentDelete/<int:id>',studentDelete,name='studentDelete'),
]
