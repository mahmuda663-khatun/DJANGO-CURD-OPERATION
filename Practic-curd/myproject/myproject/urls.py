
from django.contrib import admin
from django.urls import path
from myapp.views import*
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('teacherList/',teacherList,name='teacherList'),
    path('teacherADD/',teacherADD, name='teacherADD'),
    path('teacherDelete/<int:id>/',teacherDelete,name='teacherDelete'),
    path('teacherUpdate/<int:id>/',teacherUpdate,name='teacherUpdate'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
