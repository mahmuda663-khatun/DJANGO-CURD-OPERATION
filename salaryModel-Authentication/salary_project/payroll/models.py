from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class AuthUserModel(AbstractUser):
    company_name=models.CharField(null=True)

    def __str__(self):
        return self.username
    
class SalaryModel(models.Model):
    empolyee_name=models.CharField(null=True)
    employee_photo=models.ImageField(upload_to='img/',null=True)
    basic_salary=models.IntegerField(null=True)
    har=models.IntegerField(null=True)
    bonus=models.IntegerField(null=True)
    tax_percentage=models.DecimalField(max_digits=10,decimal_places=2,null=True)
    gross_salary=models.IntegerField(null=True)
    net_salary=models.IntegerField(null=True)

    def __str__(self):
        return self.empolyee_name
    
