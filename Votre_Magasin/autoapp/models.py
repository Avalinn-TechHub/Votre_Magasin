from django.db import models

# Create your models here.

class Auto_reg(models.Model):
    Name = models.CharField(max_length=30)
    Vehicleno = models.CharField(max_length=30)
    Phonenum = models.CharField(max_length=13)
    Address = models.CharField(max_length=50)
    Latitude = models.CharField(max_length=30)
    Longitude = models.CharField(max_length=30)
    Username = models.CharField(max_length=30)
    Password = models.CharField(max_length=30)
    Status = models.CharField(max_length=10)

class Auto_notification(models.Model):
    Pid = models.IntegerField
    sname = models.CharField(max_length=30)
    splace = models.CharField(max_length=50) #shopaddress
    uname = models.CharField(max_length=30)
    cname = models.CharField(max_length=30)
    items = models.CharField(max_length=30)
    categry = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    total = models.CharField(max_length=30)
    datetime = models.CharField(max_length=30)
    status = models.CharField(max_length=30)

class Auto_status(models.Model):
    name = models.CharField(max_length=30)
    status = models.CharField(max_length=30)