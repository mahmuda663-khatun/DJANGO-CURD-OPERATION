
from django.contrib import admin
from django.urls import path
from payroll.views import*
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('signup/',signup,name='signup'),
    path('signin/',signin,name='signin'),
    path('salarylist/',salarylist,name='salarylist'),
    path('addSalary/',addSalary,name='addSalary'),
    path('editSalary/<int:id>/',editSalary, name='editSalary'),
    path('deletesalary/<int:id>/',deletesalary,name='deletesalary'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
