
from django.contrib import admin
from django.urls import path
from myapp.views import*
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('signup/',signUp,name='signUp'),
    path('signin/',signin,name='signin'),
    path('signOut/',signOut,name='signOut'),
]
