from django.db import models

# Create your models here.
class studentModel(models.Model):
    name=models.CharField(max_length=50,null=True)
    age=models.IntegerField(null=True)
    address=models.TextField(null=True)

    def __str__(self):
        return self.name
    