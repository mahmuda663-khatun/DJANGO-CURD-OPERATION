from django.db import models

# Create your models here.
class productModel(models.Model):
    name=models.CharField(max_length=100,null=True)
    description=models.TextField(null=True)
    price=models.DecimalField(max_digits=50,decimal_places=2,null=True)
    date=models.DateField(null=True)

    def __str__(self):
        return self.name
