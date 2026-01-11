from django.db import models
from product.models import*
# Create your models here.
class ProductModel(models.Model):
    name=models.TextField(null=True)
    description=models.TextField(null=True)
    price=models.IntegerField(null=True)
    date=models.DateField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to='img/',null=True)

