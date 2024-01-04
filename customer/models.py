from django.db import models

# Create your models here.

class Customer(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    contact=models.CharField(max_length=200)

class Tasks(models.Model):
    email=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    status=models.IntegerField()
    addedOn=models.DateField()
    completedOn=models.DateField(null=True)
    removedOn=models.DateField(null=True)
