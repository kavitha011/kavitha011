from django.db import models

#create your models here.
class student(models.Model):
    name=models.CharField(max_length=20)
    rollno=models.IntegerField()
    email=models.EmailField()

def __str__(self):
    return(self.name)

