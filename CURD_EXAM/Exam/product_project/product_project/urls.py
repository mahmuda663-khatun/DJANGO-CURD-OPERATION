
from django.contrib import admin
from django.urls import path
from product.views import*
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('productList/',productList,name='productList'),
    path('productAdd/',productAdd,name='productAdd'),
    path('productUpdate/<int:id>/',productUpdate,name='productUpdate'),
    path('productDelete/<int:id>/',productDelete,name='productDelete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
