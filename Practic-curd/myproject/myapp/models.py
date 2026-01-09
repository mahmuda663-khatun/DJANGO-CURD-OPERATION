from django.db import models
from myapp.models import *
# Create your models here.
class teacherModel(models.Model):
    name=models.CharField(max_length=50, null=True)
    department=models.CharField(null=True)
    email=models.EmailField(null=True)
    joininjdate=models.DateField(null=True)
    salay=models.PositiveIntegerField(null=True)
    picture=models.ImageField(upload_to='img/',null=True)

    # def __str__(self):
    #     return self.name
    
    