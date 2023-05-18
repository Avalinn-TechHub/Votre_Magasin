from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from shopapp.models import Shop_reg
from autoapp.models import Auto_reg
from customerapp.models import Customer_reg


# Create your views here.
# --------------------------------------------------
# login home page load
# --------------------------------------------------

def loginhome(request):
    return render(request, "login/index.html")




# --------------------------------------------------
# about page load
# --------------------------------------------------

def l_about(request):
    return render(request, "login/about.html")


# --------------------------------------------------
# contact page load
# --------------------------------------------------

def l_contact(request):
    return render(request, "login/contact.html")



# --------------------------------------------------
# load shop home page
# --------------------------------------------------

def shophome(request):
    return render(request, "shop/index.html")


# --------------------------------------------------
# load login page
# --------------------------------------------------

def loginpage(request):
    return render(request, "login/Login.html")


# --------------------------------------------------
# load shop registration page
# --------------------------------------------------

def shopregistration(request):
    return render(request, "login/shopkeeper.html")


# --------------------------------------------------
# insert shop owner details into shop_reg table
# --------------------------------------------------

def insert_shop_reg(request):
    if request.method == "POST":
        obj = Shop_reg()
        obj.Name = request.POST.get('name')
        obj.Email = request.POST.get('email')
        obj.Phonenum = request.POST.get('phone')
        obj.Address = request.POST.get('address')
        obj.Latitude = request.POST.get('latitude')
        obj.Longitude = request.POST.get('longitude')
        obj.Username = request.POST.get('username')
        obj.Password = request.POST.get('password')
        obj.Status = "Inactive"
        obj.save()
        return render(request, "login/index.html")
    else:
        return render(request, "login/Login.html")


# -----------------------------------------------------------------------------------
# logging in using username password and usertype admin=0,shop=1 auto=2 customer=3
# -----------------------------------------------------------------------------------

def checklogin(request):
    usertype = request.POST.get("ddlroletyp")
    uname = request.POST.get("username")
    pswrd = request.POST.get("password")
    if usertype == "0":  # admin
        if uname == "admin" and pswrd == "admin":
            return render(request, "admin/index.html")
    elif usertype == "1":  # shop owner
        if Shop_reg.objects.filter(Username=uname, Password=pswrd, Status="Active").exists():
            suser = Shop_reg.objects.get(Username=uname, Password=pswrd)
            request.session['userid'] = suser.id
            request.session['username'] = uname
            return render(request, "shop/index.html")
        else:
            return render(request, "login/Login.html", {'Error': ' Invalid '})
    elif usertype == "2":  # Auto
        if Auto_reg.objects.filter(Username=uname, Password=pswrd, Status="Active").exists():
            auser = Auto_reg.objects.get(Username=uname, Password=pswrd)
            request.session['userid'] = auser.id
            request.session['username'] = uname
            return render(request, "auto/index.html")
        else:
            return render(request, "login/Login.html", {'Error': ' Invalid '})
    elif usertype == "3":  # Customer
        if Customer_reg.objects.filter(Username=uname, Password=pswrd).exists():
            cuser = Customer_reg.objects.get(Username=uname, Password=pswrd)
            request.session['userid'] = cuser.id
            request.session['username'] = uname
            return render(request, "customer/index.html")
        else:
            return render(request, "login/Login.html", {'Error': ' Invalid '})


    else:
        return render(request, "404.html")


# --------------------------------------------------
# load auto registration page
# --------------------------------------------------

def autoregistration(request):
    return render(request, "login/autoservice.html")


# --------------------------------------------------
# insert values into auto_reg table
# --------------------------------------------------

def insert_auto_reg(request):
    if request.method == "POST":
        obj = Auto_reg()
        obj.Name = request.POST.get('name')
        obj.Vehicleno = request.POST.get('vehicleno')
        obj.Phonenum = request.POST.get('phone')
        obj.Address = request.POST.get('address')
        obj.Latitude = request.POST.get('latitude')
        obj.Longitude = request.POST.get('longitude')
        obj.Username = request.POST.get('username')
        obj.Password = request.POST.get('password')
        obj.Status = "Inactive"
        obj.save()
        return render(request, "login/index.html")
    else:
        return render(request, "login/Login.html")


# --------------------------------------------------
# LOAD CUSTOMER REGISTRATION PAGE
# --------------------------------------------------

def customer_registration(request):
    return render(request, "login/customer.html")


# --------------------------------------------------
# INSERT VALUES INTO CUSTOMER_REG TABLE
# --------------------------------------------------

def insert_customer_reg(request):
    if request.method == "POST":
        obj = Customer_reg()
        obj.Name = request.POST.get('name')
        obj.Email = request.POST.get('email')
        obj.Phonenum = request.POST.get('phone')
        obj.Address = request.POST.get('address')
        obj.Username = request.POST.get('username')
        obj.Password = request.POST.get('password')
        obj.save()
        return render(request, "login/index.html")
    else:
        return render(request, "login/Login.html")
