from django.db import models
from myapp.models import*
# Create your models here.
class studentModel(models.Model):
    Name=models.TextField(null=True)
    Roll=models.PositiveIntegerField(null=True)
    Address=models.TextField(null=True)
    Image=models.ImageField(upload_to='img/',null=True)
    Date=models.DateTimeField(null=True)

def __str__(self):
    return self.name
