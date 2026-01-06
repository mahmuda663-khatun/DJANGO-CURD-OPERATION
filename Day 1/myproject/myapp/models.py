from django.db import models

# Create your models here.
class studentModel(models.Model):
    name=models.CharField(max_length=100,null=True)
    age=models.IntegerField(null=True)
    about=models.TextField(null=True)

    def__str__(self):
        return self.name
    