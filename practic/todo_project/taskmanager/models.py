from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class AuthUserModel(AbstractUser):
    USER_TYPE=[
        ('Admin','Admin'),
        ('User','User'),
    ]
    full_name=models.CharField(null=True)
    user_type=models.CharField(choices=USER_TYPE,null=True)

    def __str__(self):
        return self.username