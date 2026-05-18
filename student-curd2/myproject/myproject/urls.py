
from django.contrib import admin
from django.urls import path
from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home ,name='home'),
    path('student_list/', student_list ,name='student_list'),
    path('student_add/', student_add ,name='student_add'),
    path('student_update/<int:id>', student_update ,name='student_update'),
    path('student_delete/<int:id>', student_delete ,name='student_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
