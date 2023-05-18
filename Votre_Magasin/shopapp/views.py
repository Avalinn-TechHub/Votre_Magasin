from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
import json
from .models import *
from adminapp.models import Category, Sub_category
from customerapp.models import Cart, Purchase, Customer_reg, Auto_booking
from shopapp.models import Product, Shop_reg
from autoapp.models import Auto_reg, Auto_notification, Auto_status
from datetime import datetime
from django.contrib import messages


# Create your views here.

# --------------------------------------------------
# load home page
# --------------------------------------------------

def shophome(request):
    return render(request, "shop/index.html")


# --------------------------------------------------
# About page load
# --------------------------------------------------

def shopabout(request):
    return render(request, "shop/about.html")


# --------------------------------------------------
# Contact page load
# --------------------------------------------------

def shopcontact(request):
    return render(request, "shop/contact.html")


# --------------------------------------------------
# 404 page load
# --------------------------------------------------

def shoperror(request):
    return render(request, "shop/404.html")


# --------------------------------------------------
# load addproduct form
# --------------------------------------------------

def load_addproduct(request):
    data = Category.objects.all()  # fetching values from category table to store in ddlcategory
    data2 = Sub_category.objects.all()  # fetching values from subcategory table to store in ddlsubcategory
    return render(request, "shop/Addproduct.html", {'cat': data, 'subcat': data2})


# --------------------------------------------------
# insert data to product table
# --------------------------------------------------

def insert_addproduct(request):
    if request.method == "POST":
        obj = Product()
        obj.Pname = request.POST.get('productname')
        obj.Categry = request.POST.get('ddlcategory')
        obj.Subcat = request.POST.get('ddlsubcategory')
        obj.Price = request.POST.get('proprice')
        obj.Info = request.POST.get('description')
        obj.Stock = request.POST.get('instock')
        obj.Username = request.session['username']
        if len(request.FILES) != 0:
            obj.Image = request.FILES['image']  # storing image url to table
        obj.save()
        messages.success(request, 'Product added sucessfully')
        return redirect('/shopapp/load_addproduct')
    else:
        return render(request, "shop/404.html")


def handle_uploaded_file(f, name):
    filename = 'uploads' + str(name)
    with open(filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


# --------------------------------------------------
# view profile details of logged in shop owner
# --------------------------------------------------

def viewprofile(request):
    uname = request.session['username']
    data = Shop_reg.objects.get(Username=uname)  # select * from shop_reg where username = session username
    return render(request, "shop/myprofile.html", {'profile': data})


# --------------------------------------------------
# update user profile
# --------------------------------------------------

def update_profile(request):
    if request.method == "POST":
        obj = Shop_reg()
        id = request.session['userid']
        obj.id = id
        obj.Name = request.POST.get('name')
        obj.Email = request.POST.get('email')
        obj.Phonenum = request.POST.get('phone')
        obj.Address = request.POST.get('address')
        obj.Latitude = request.POST.get('latitude')
        obj.Longitude = request.POST.get('longitude')
        obj.Username = request.POST.get('username')
        obj.Password = request.POST.get('password')
        obj.Status = request.POST.get('status')
        obj.save()
        return redirect('/shopapp/viewprofile')


# --------------------------------------------------
# view products details of logged in shop owner
# --------------------------------------------------

def viewproducts(request):
    uname = request.session['username']
    data = Product.objects.filter(Username=uname).exists()  # select * from products where username = session username
    data2 = Product.objects.all()
    return render(request, "shop/shop_products_view.html", {'products': data2})


# --------------------------------------------------
# load update_product.html page
# --------------------------------------------------

def load_update_product(request, id):
    data = Product.objects.get(id=id)
    data1 = Category.objects.all()  # fetching values from category table to store in ddlcategory
    data2 = Sub_category.objects.all()  # fetching values from subcategory table to store in ddlsubcategory
    return render(request, "shop/update_product.html", {'pro': data, 'cat': data1, 'subcat': data2})


# --------------------------------------------------
# Update the Products by shop owner
# --------------------------------------------------

def update_product(request, id):
    obj = Product()
    obj.id = id
    obj.Pname = request.POST.get('productname')
    obj.Categry = request.POST.get('ddlcategory')
    obj.Subcat = request.POST.get('ddlsubcategory')
    obj.Price = request.POST.get('proprice')
    obj.Info = request.POST.get('description')
    obj.Stock = request.POST.get('instock')
    obj.Username = request.session['username']
    if len(request.FILES) != 0:
        obj.Image = request.FILES['image']
    obj.save()
    messages.success(request, 'Product updated sucessfully')
    return redirect('/shopapp/viewproducts')



# --------------------------------------------------
# Orders
# --------------------------------------------------

def load_orders(request):
    uname = request.session['username']
    data= Purchase.objects.filter(shopname=uname)
    return render(request, "shop/orders.html", {'orders': data})



# --------------------------------------------------
# clearing the session id of user by logging out
# --------------------------------------------------

def logout(request):
    del request.session['userid']
    del request.session['username']
    return render(request, "login/Login.html")
