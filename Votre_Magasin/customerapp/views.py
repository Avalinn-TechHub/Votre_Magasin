from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from customerapp.models import Cart, Purchase, Customer_reg, Auto_booking
from shopapp.models import Product, Shop_reg
from autoapp.models import Auto_reg, Auto_notification, Auto_status


# Create your views here.

# --------------------------------------------------
# customer home page load
# --------------------------------------------------

def home(request):
    return render(request, "customer/index.html")


# --------------------------------------------------
# 404 error page load
# --------------------------------------------------

def cerror(request):
    return render(request, "customer/404.html")


# --------------------------------------------------
# about page load
# --------------------------------------------------

def c_about(request):
    return render(request, "customer/about.html")


# --------------------------------------------------
# contact page load
# --------------------------------------------------

def c_contact(request):
    return render(request, "customer/contact.html")


# --------------------------------------------------
# my profile page load
# --------------------------------------------------

def c_myprofile(request):
    uname = request.session['username']
    data = Customer_reg.objects.get(Username=uname)  # select * from customer_reg where username = session username
    return render(request, "customer/myprofile.html", {'profile': data})


# --------------------------------------------------
# update user profile
# --------------------------------------------------

def c_update_profile(request):
    if request.method == "POST":
        obj = Customer_reg()
        id = request.session['userid']
        obj.id = id
        obj.Name = request.POST.get('name')
        obj.Email = request.POST.get('email')
        obj.Phonenum = request.POST.get('phone')
        obj.Address = request.POST.get('address')
        obj.Username = request.POST.get('username')
        obj.Password = request.POST.get('password')
        obj.save()
        return redirect('/customerapp/c_myprofile')


# --------------------------------------------------
# view products page load
# --------------------------------------------------

def c_view_products(request):
    data2 = Product.objects.all()
    return render(request, "customer/user_products_view.html", {'products': data2})


# --------------------------------------------------
# add to cart button on products view page
# --------------------------------------------------

def add_to_cart(request, id):
    uname = request.session['username']
    qty = 1
    cuser = Product.objects.get(id=id)
    Itemid = cuser.id
    Shopname = cuser.Username
    product = cuser.Pname
    Catgry = cuser.Categry
    Price = cuser.Price
    Total = cuser.Price
    img = cuser.Image
    obj = Cart()
    obj.Itemid = Itemid
    obj.Shopname = Shopname
    obj.Userid = uname
    obj.Product = product
    obj.Image = img
    obj.Catgry = Catgry
    obj.Price = Price
    obj.Quantity = qty
    obj.Total = Total * int(qty or 1)
    obj.Status = "Unpaid"
    obj.save()
    return redirect('/customerapp/cart')


# else:
#  return render(request, "customer/404.html")


# --------------------------------------------------
# cart page load
# --------------------------------------------------

def cart(request):
    uname = request.session['username']
    data = Cart.objects.filter(Userid=uname, Status="Unpaid").exists()
    data2 = Cart.objects.all()
    d = Cart.objects.filter(Userid=uname, Status="Unpaid")
    tot = 0
    for item in d:
        tot = int(tot) + int(item.Total)
    gtot = tot + 50  # grand total
    return render(request, "customer/cart.html", {'cart': data2, 'tot': tot, 'gtot': gtot, })


# --------------------------------------------------
# delete item from cart
# --------------------------------------------------

def delete_cart(request, id):
    uname = request.session['username']
    data = Cart.objects.get(id=id, Userid=uname)
    data.delete()
    return redirect('/customerapp/cart')


# --------------------------------------------------
# edit quantity in cart
# --------------------------------------------------

def edit_cart(request, id):
    uname = request.session['username']
    data = Cart.objects.get(id=id, Userid=uname)
    return render(request, "customer/update_quantity.html", {'up': data})


# --------------------------------------------------
# update item quantity from cart
# --------------------------------------------------

def update_quantity(request, id):
    uname = request.session['username']
    if request.method == "POST":
        qt = request.POST.get('quantity')
        data = Cart.objects.get(id=id, Userid=uname)
        img = data.Image
        data.Shopname = request.POST.get("shopname")
        data.Userid = uname
        data.Itemid = request.POST.get("itemid")
        data.Product = data.Product
        data.Image = img
        data.Catgry = data.Catgry
        data.Price = data.Price
        data.Quantity = qt
        t = data.Price
        tot = int(t) * int(qt)
        data.Total = tot
        data.Status = "Unpaid"
        data.save()
        return redirect('/customerapp/cart')


# --------------------------------------------------
# load shipping address,Auto and products from cart in checkout page
# --------------------------------------------------

def load_checkout(request):
    uname = request.session['username']
    # fetching customer details
    cust = Customer_reg.objects.get(Username=uname)  # select * from customer_reg where username = session username
    # fetching products from cart
    data = Cart.objects.filter(Userid=uname, Status="Unpaid").exists()
    data2 = Cart.objects.all()
    d = Cart.objects.filter(Userid=uname, Status="Unpaid")
    tot = 0
    for item in d:
        tot = int(tot) + int(item.Total)
    gtot = tot + 50  # grand total
    # fetching auto
    auto = Auto_reg.objects.all()
    return render(request, "customer/checkout.html",
                  {'profile': cust, 'cart': data2, 'tot': tot, 'gtot': gtot, 'auto': auto})


# --------------------------------------------------
# place order button in checkout page
# --------------------------------------------------

def place_order(request):
    uname = request.session['username']
    auto = request.POST.get('ddlauto')
    if request.method == "POST":
        data = Cart.objects.filter(Userid=uname, Status="Unpaid").exists()
        data2 = Cart.objects.all()
        for i in data2:
            Snames = i.Shopname
            item = i.Product
            category = i.Catgry
            prce = i.Price
            tot = i.Total
            qt = int(i.Quantity)
            date = datetime.date.today()

            # moving values from cart to purchase table
            obj = Purchase()
            p = obj.id
            obj.shopname = Snames
            obj.Username = uname
            obj.items = item
            obj.catgry = category
            obj.price = prce
            obj.total = tot
            obj.date = date
            obj.Autoname = auto
            obj.Status = "Pending"
            obj.save()

            #  update stock in product table
            obj1 = Product.objects.get(Pname=i.Product)
            s1 = obj1.Stock
            Product.objects.filter(Pname=i.Product).update(Stock=s1 - qt)

            # Adding details to auto_notifications about the order
            obj2 = Auto_notification()
            obj2.Pid = p
            # fetch shop name and address
            place = Shop_reg.objects.get(Username=Snames)
            addr = place.Address
            snam = place.Name
            obj2.sname = snam
            obj2.splace = addr
            obj2.uname = auto
            # fetch customer name
            n = Customer_reg.objects.get(Username=uname)
            na = n.Name
            obj2.cname = na
            obj2.items = item
            obj2.categry = category
            obj2.price = prce
            obj2.total = tot
            obj2.datetime = date
            obj2.status = "Not Approved"
            obj2.save()

            # delete from cart table
            i.delete()
    return redirect('/customerapp/c_view_products')


# --------------------------------------------------
# My orders page load
# --------------------------------------------------

def myorders(request):
    uname = request.session['username']
    data = Purchase.objects.filter(Username=uname)
    data2 = Auto_booking.objects.filter(Cusername=uname)
    return render(request, "customer/myorders.html", {'purchase': data , 'auto': data2})


# --------------------------------------------------
# auto booking page load
# --------------------------------------------------

def load_auto_booking(request):
    uname = request.session['username']
    data = Auto_status.objects.get(status="Available")
    aname= data.name
    n = Auto_reg.objects.filter(Username=aname)
    data2 = Customer_reg.objects.get(Username=uname)
    return render(request, "customer/book_auto.html", {'auto':n, 'profile': data2})



# --------------------------------------------------
# bookauto button on auto booking page
# --------------------------------------------------


def book_auto(request):
    uname = request.session['username']
    data = Customer_reg.objects.get(Username=uname)
    na = data.Name
    ph= data.Phonenum
    ad = data.Address
    auto= request.POST.get('ddlauto')
    data2 = Auto_reg.objects.get(Name=auto)
    usn = data2.Username
    veh= data2.Vehicleno
    phn=data2.Phonenum
    dat= datetime.date.today()
    if request.method == "POST":
        obj = Auto_booking()
        obj.Cname = na
        obj.Cusername = uname
        obj.Cphone = ph
        obj.Cplace = ad
        obj.Aname = auto
        obj.Ausername = usn
        obj.Avehicleno = veh
        obj.Aphone = phn
        obj.Date =dat
        obj.Status = "Requested"
        obj.save()
    return redirect('/customerapp/load_auto_booking')

# --------------------------------------------------
# clearing the session id of user by logging out
# --------------------------------------------------

def c_logout(request):
    del request.session['userid']
    del request.session['username']
    return render(request, "login/Login.html")

# update code
#  Cart.objects.filter(Userid=uname, Status="Unpaid").update(Status="Paid")
# else:
#  return render(request, "customer/404.html")
