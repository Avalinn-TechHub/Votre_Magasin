from django.db import models

# Create your models here.

class Category(models.Model):
    Categry = models.CharField(max_length=30)

class Sub_category(models.Model):
    Subcategory = models.CharField(max_length=30)
    Categry = models.CharField(max_length=30)

