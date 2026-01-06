from django.db import models
from myapp.models import *
# Create your models here.
class productModel(models.Model):
    name=models.CharField(max_length=100,null=True)
    description=models.TextField(null=True)
    price=models.DecimalField(max_digits=10,decimal_places=2,null=True)
    created_at=models.DateField(auto_now_add=True)
    mark=models.PositiveIntegerField(null=True)
    grade=models.CharField(null=True)

# salary model 
class slaryModel(models.Model):
    hra=models.CharField(max_length=200)
    basic_salary=models.IntegerField(null=True)
    overtime_hours=models.IntegerField(null=True)
    hra_percent=models.DecimalField(max_digits=5,decimal_places=2,null=True)
    da_percent=models.DecimalField(max_digits=5,decimal_places=2,null=True)
    ta_persent=models.DecimalField(max_digits=5,decimal_places=2,null=True)
    DA=models.DecimalField(max_digits=5,decimal_places=2,null=True)
    TA=models.DecimalField(max_digits=5,decimal_places=2,null=True)
    overtime=models.IntegerField(null=True)
    bouns=models.DecimalField(max_digits=5,decimal_places=2,null=True)
    GrossSalary=models.DecimalField(max_digits=5,decimal_places=2,null=True)













