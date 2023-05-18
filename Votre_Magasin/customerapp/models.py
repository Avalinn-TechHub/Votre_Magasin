from django.db import models


# Create your models here.

class Customer_reg(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.CharField(max_length=30)
    Phonenum = models.CharField(max_length=13)
    Address = models.CharField(max_length=50)
    Username = models.CharField(max_length=30)
    Password = models.CharField(max_length=30)


class Auto_booking(models.Model):
    Cname = models.CharField(max_length=30)
    Cusername = models.CharField(max_length=30)
    Cphone = models.CharField(max_length=13)
    Cplace = models.CharField(max_length=30)
    Aname = models.CharField(max_length=30)
    Ausername = models.CharField(max_length=30)
    Avehicleno = models.CharField(max_length=30)
    Aphone = models.CharField(max_length=13)
    Date = models.DateField()
    Status = models.CharField(max_length=10)


class Purchase(models.Model):
    shopname = models.CharField(max_length=30)
    Username  = models.CharField(max_length=30)
    items  = models.CharField(max_length=30)
    catgry = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    total = models.CharField(max_length=30)
    date = models.DateField(max_length=30)
    Autoname = models.CharField(max_length=30)
    Status = models.CharField(max_length=10)

class Cart(models.Model):
    Shopname = models.CharField(max_length=30)
    Userid = models.CharField(max_length=30)
    Itemid = models.CharField(max_length=30)
    Product = models.CharField(max_length=30)
    Catgry = models.CharField(max_length=30)
    Price = models.CharField(max_length=30)
    Image = models.CharField(max_length=30)
    Quantity =models.IntegerField(max_length=5)
    Total = models.IntegerField(max_length=30)
    Status = models.CharField(max_length=10)


