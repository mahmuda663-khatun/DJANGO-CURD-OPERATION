
from django.contrib import admin
from django.urls import path
from myapp.views import*
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('studentList/',studentList,name='studentList'),
    path('studentADD/',studentADD,name='studentADD'),
    path('studentUpdate/<int:id>',studentUpdate,name='studentUpdate'),
    path('studentDelete/<int:id>',studentDelete,name='studentDelete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
