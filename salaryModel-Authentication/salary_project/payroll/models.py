from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class AuthUserModel(AbstractUser):
    company_name=models.CharField(null=True)

    def __str__(self):
        return self.username
    
class SalaryModel(models.Model):
    empolyee_name=models.CharField(null=True)
    employee_photo=models.ImageField(upload_to='img/',null=True)
    basic_salary=models.IntegerField(null=True)
    har=models.IntegerField(null=True)
    bonus=models.IntegerField(null=True)
    tax_percentage=models.DecimalField(max_digits=10,decimal_places=2,null=True)
    gross_salary=models.IntegerField(null=True)
    net_salary=models.IntegerField(null=True)

    def __str__(self):
        return self.empolyee_name
    
class subjectModel(models.Model):
        DEPT_TYPES = [
             ('CSE','CSE'),
             ('EEE','EEE'),
             ('CIVIL','CIVIL')
        ]
        subject_name = models.CharField(max_length=200, null=True)
        description = models.TextField(null=True)
        dept_type = models.CharField(choices=DEPT_TYPES,max_length=10,null=True)
        credit = models.PositiveIntegerField(null=True)

        def __str__(self):
            return f'{self.subject_name}' 