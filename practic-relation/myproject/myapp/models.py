from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class UserModel(AbstractUser):
    USER_TYPE=[
        ('Admin','Admin'),
        ('User','User'),
    ]
    user_type=models.CharField(choices=USER_TYPE,null=True)

    def __str__(self):
        return self.username

class DepartModel(models.Model):
    name=models.CharField(null=True)
    description=models.TextField(null=True)

    def __str__(self):
        return self.name

class EmployeModel(models.Model):
    name=models.CharField(null=True)
    age=models.PositiveIntegerField(null=True)
    image=models.ImageField(upload_to='img/', null=True)
    department=models.ForeignKey(DepartModel ,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class SalaryModel(models.Model):
    basic_salary=models.IntegerField(null=True)
    bonus=models.IntegerField(null=True)
    employee=models.ForeignKey(EmployeModel, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.employee