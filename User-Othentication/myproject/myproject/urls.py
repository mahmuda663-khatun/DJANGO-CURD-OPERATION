
from django.contrib import admin
from django.urls import path
from myapp.views import*
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',HomePage,name='home'),
    path('',SignInPage,name='signin'),
    path('signup/',SignUpPage,name='signup'),
    path('signout/',logoutPage,name='signout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
