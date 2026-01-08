from django.db import models
from myapp.models import*
# Create your models here.
class salaryModel(models.Model):
    Bouns=models.IntegerField(null=True)
    Basic_salary=models.IntegerField(null=True)
    overtime_hours=models.IntegerField(null=True)
    ta_percent=models.DecimalField(max_digits=50,decimal_places=2,null=True)
    da_percent=models.DecimalField(max_digits=50,decimal_places=2,null=True)
    her_percent=models.DecimalField(max_digits=50,decimal_places=2,null=True)
    Gross_salary=models.IntegerField(null=True)
    Picture=models.ImageField(upload_to='img/',null=True)
def __str__(self):
    return self.name

    
