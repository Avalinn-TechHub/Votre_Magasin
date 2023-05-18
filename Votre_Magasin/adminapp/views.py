from django.shortcuts import render, redirect
from django.http import HttpResponse
from shopapp.models import Shop_reg
from autoapp.models import Auto_reg
from .models import *


# Create your views here.
# --------------------------------------------------
# home page load
# --------------------------------------------------

def home(request):
    return render(request, "admin/index.html")


# --------------------------------------------------
# About page load
# --------------------------------------------------

def adminabout(request):
    return render(request, "admin/about.html")


# --------------------------------------------------
# Contact page load
# --------------------------------------------------

def admincontact(request):
    return render(request, "admin/contact.html")


# --------------------------------------------------
# 404 page load
# --------------------------------------------------

def error(request):
    return render(request, "admin/404.html")


# --------------------------------------------------
# view/approve shop page load
# --------------------------------------------------

def viewshop(request):
    shop = Shop_reg.objects.all()
    return render(request, "admin/viewstore.html", {'Shop': shop})


# --------------------------------------------------
# load approve shop page
# --------------------------------------------------

def load_approveform(request, id):
    shop = Shop_reg.objects.get(id=id)
    return render(request, "admin/approveshop.html", {'Shop': shop})


# -----------------------------------------------------------------------------
# approve button (approveshop.html page) function to change status to Active
# -----------------------------------------------------------------------------

def approvestore(request, id):
    obj = Shop_reg()
    obj.id = id
    obj.Name = request.POST.get('name')
    obj.Email = request.POST.get('email')
    obj.Phonenum = request.POST.get('phone')
    obj.Address = request.POST.get('address')
    obj.Latitude = request.POST.get('latitude')
    obj.Longitude = request.POST.get('longitude')
    obj.Username = request.POST.get('username')
    obj.Password = request.POST.get('password')
    obj.Status = "Active"
    obj.save()
    return redirect('/adminapp/viewshop')


# --------------------------------------------------
# disapprove function in view/approve shop page
# --------------------------------------------------

def disapproveshop(request, id):
    shop = Shop_reg.objects.get(id=id)
    shop.delete()
    return redirect('/adminapp/viewshop')


# --------------------------------------------------
# view/approve auto page load
# --------------------------------------------------

def viewauto(request):
    auto = Auto_reg.objects.all()
    return render(request, "admin/viewauto.html", {'Auto': auto})


# --------------------------------------------------
# load approve auto page
# --------------------------------------------------

def load_approveauto(request, id):
    auto = Auto_reg.objects.get(id=id)
    return render(request, "admin/approveauto.html", {'Auto': auto})


# ----------------------------------------------------------------------------
# approve button (approveauto.html page) function to change status to Active
# ----------------------------------------------------------------------------

def approveauto(request, id):
    obj = Auto_reg()
    obj.id = id
    obj.Name = request.POST.get('name')
    obj.Vehicleno = request.POST.get('vehicleno')
    obj.Phonenum = request.POST.get('phone')
    obj.Address = request.POST.get('address')
    obj.Latitude = request.POST.get('latitude')
    obj.Longitude = request.POST.get('longitude')
    obj.Username = request.POST.get('username')
    obj.Password = request.POST.get('password')
    obj.Status = "Active"
    obj.save()
    return redirect('/adminapp/viewauto')


# --------------------------------------------------
# disapprove function in view/approve auto page
# --------------------------------------------------

def disapproveauto(request, id):
    auto = Auto_reg.objects.get(id=id)
    auto.delete()
    return redirect('/adminapp/viewauto')


# --------------------------------------------------
# load category page
# --------------------------------------------------

def category(request):
    return render(request, "admin/addcategory.html")


# --------------------------------------------------
# add category
# --------------------------------------------------

def addcategory(request):
    if request.method == "POST":
        obj = Category()
        obj.Categry = request.POST.get('category')
        obj.save()
        return redirect('/adminapp/category')
    else:
        return render(request, "admin/404.html")


# --------------------------------------------------
# load subcategory page
# --------------------------------------------------

def subcategory(request):
    data = Category.objects.all()  # select * from category
    return render(request, "admin/subcategory.html", {'cat': data})


# --------------------------------------------------
# add subcategory
# --------------------------------------------------

def addsubcategory(request):
    if request.method == "POST":
        obj = Sub_category()
        obj.Categry = request.POST.get('ddlcategory')
        obj.Subcategory = request.POST.get('subcategory')
        obj.save()
        return redirect('/adminapp/subcategory')
    else:
        return render(request, "admin/404.html")


# --------------------------------------------------
# view category
# --------------------------------------------------

def viewcategory(request):
    cat = Category.objects.all()
    return render(request, "admin/view_category.html", {'cat': cat})


# --------------------------------------------------
# load update_category.html page
# --------------------------------------------------

def load_update_category(request, id):
    cat = Category.objects.get(id=id)
    return render(request, "admin/update_category.html", {'cat': cat})


# --------------------------------------------------
# update button in update_category.html
# --------------------------------------------------

def update_category(request, id):
    obj = Category()
    obj.id = id
    obj.Categry = request.POST.get('category')
    obj.save()
    return redirect('/adminapp/viewcategory')


# --------------------------------------------------
# view subcategory
# --------------------------------------------------

def viewsubcategory(request):
    data = Sub_category.objects.all()  # select * from category
    return render(request, "admin/view_subcategory.html", {'subcat': data})


# --------------------------------------------------
# load update_subcategory.html page
# --------------------------------------------------

def load_update_subcategory(request, id):
    data = Sub_category.objects.get(id=id)
    data2 = Category.objects.all()
    return render(request, "admin/update_subcategory.html", {'subcat': data, 'cat': data2})


# --------------------------------------------------
# update button in update_subcategory.html
# --------------------------------------------------

def update_subcategory(request, id):
    obj = Sub_category()
    obj.id = id
    obj.Categry = request.POST.get('ddlcategory')
    obj.Subcategory = request.POST.get('subcategory')
    obj.save()
    return redirect('/adminapp/viewsubcategory')



# --------------------------------------------------
# clearing the session id of user by logging out
# --------------------------------------------------

def adlogout(request):
    return render(request, "login/Login.html")
