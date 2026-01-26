
from django.contrib import admin
from django.urls import path
from myapp.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home,name='home'),
    path('',signup,name='signup'),
    path('signin/',signin,name='signin'),
    path('signout/',signout,name='signout'),
    path('dep_list/',dep_list,name='dep_list'),
    path('dep_Add/',dep_Add,name='dep_Add'),
    path('dep_Edit/<int:id>/',dep_Edit,name='dep_Edit'),
    path('dep_Delete/<int:id>/',dep_Delete,name='dep_Delete'),
]
