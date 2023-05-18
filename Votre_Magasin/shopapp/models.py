from django.db import models

# Create your models here.

class Shop_reg(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.CharField(max_length=30)
    Phonenum = models.CharField(max_length=13)
    Address = models.CharField(max_length=50)
    Latitude = models.CharField(max_length=30)
    Longitude = models.CharField(max_length=30)
    Username = models.CharField(max_length=30)
    Password = models.CharField(max_length=30)
    Status = models.CharField(max_length=10)


class Product(models.Model):
    Pname = models.CharField(max_length=30)
    Categry = models.CharField(max_length=30)
    Subcat = models.CharField(max_length=30)
    Price = models.CharField(max_length=10)
    Info = models.CharField(max_length=200)
    Stock = models.IntegerField(max_length=10)
    Image = models.FileField(upload_to ='uploads')
    Username = models.CharField(max_length=30)
