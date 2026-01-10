from django.db import models
from myapp.models import*

class studentModel(models.Model):
    Name=models.CharField(null=True)
    Course=models.CharField(null=True)
    Total_Marks=models.PositiveIntegerField(null=True)
    image=models.ImageField(upload_to='imag/',null=True)

def __str__(self):
    return self .name


