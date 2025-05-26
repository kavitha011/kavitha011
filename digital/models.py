from django.db import models

#create your models here.
class student(models.Model):
    name=models.CharField(max_length=20)
    rollno=models.IntegerField()
    email=models.EmailField()

    def __str__(self):
        return self.name

class biodata(models.Model):
    age=models.IntegerField()
    birth=models.IntegerField()
    gender=models.CharField(max_length=20)
    year=models.IntegerField()
    department=models.CharField(max_length=20)
    stream=models.CharField(max_length=20)
    mobile_no=models.CharField(max_length=20)
    age=models.IntegerField()
    department=models.CharField(max_length=20)
    stream=models.CharField(max_length=20)

    def __str__(self):
        return self.title
