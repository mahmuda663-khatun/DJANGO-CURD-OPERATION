from django.db import models

# Create your models here.
class projectModel(models.Model):
    status_type=[
        ('pending','Pending'),
        ('ongoing','Ongoing'),
        ('completed','Completed'),
    ]

    projectName=models.CharField(max_length=200,null=True)
    description=models.TextField(null=True)
    status=models.CharField(choices=status_type,null=True)
    deadline=models.DateField(null=True)

     