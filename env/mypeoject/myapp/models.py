from django.db import models

class studentModel(models.Model):
    name=models.CharField(max_length=100,null=True) #choto choto text er jonno charField 
    age=models.IntegerField(null=True) # number er jonno integerfield
    about=models.TextField(null=True) # large text er jonno TextField
    
    def __str__(self):
        return self.name
    
    
    '''
    model toiri korar por makemigrations , migrate korbo 
    '''