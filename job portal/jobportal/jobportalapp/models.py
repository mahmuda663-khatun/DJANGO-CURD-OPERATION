from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class userModel(AbstractUser):
    USER_TYPE=[
      ('Siker','Siker'),
      ('Rikruter','Rikruter'),
    ]
    user_type=models.CharField(choices=USER_TYPE,null=True)

    def __str__(self):
        return self.username