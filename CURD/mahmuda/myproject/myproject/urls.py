
from django.contrib import admin
from django.urls import path
from myapp.views import*
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base,name='base'),
    path('productlist/',productlist,name='productlist'),
    path('productADD/',productADD,name='productADD'),
    path('productDelete/<int:id>/',productDelete,name='productDelete'),
    path('editproduct/<int:id>/',editproduct,name='editproduct'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
