from django.shortcuts import render, redirect
from django.http import HttpResponse
from autoapp.models import Auto_reg, Auto_notification, Auto_status
from customerapp.models import Cart, Purchase, Customer_reg, Auto_booking
from shopapp.models import Product, Shop_reg


# Create your views here.

# --------------------------------------------------
# Auto home page load
# --------------------------------------------------

def ahome(request):
    return render(request, "auto/index.html")


# --------------------------------------------------
# Auto about page load
# --------------------------------------------------

def aabout(request):
    return render(request, "auto/about.html")


# --------------------------------------------------
# Auto contact page load
# --------------------------------------------------

def acontact(request):
    return render(request, "auto/contact.html")


# --------------------------------------------------
#  load status page load
# --------------------------------------------------

def load_status(request):
    return render(request, "auto/status.html")


# --------------------------------------------------
#  update status
# --------------------------------------------------

def update_status(request):
    uname = request.session['username']
    stat = request.POST.get('Status')
    if request.method == "POST":
        obj = Auto_status()
        obj.name = uname
        if Auto_status.objects.filter(name=uname).exists():
            Auto_status.objects.filter(name=uname).update(status=stat)
        else:
            obj.status = stat
            obj.save()
        return render(request, "auto/index.html")
    else:
        return render(request, "auto/404.html")


# --------------------------------------------------
#  load notifications page
# --------------------------------------------------

def load_notifications(request):
    uname = request.session['username']
    n = Auto_reg.objects.get(Username=uname)
    name = n.Name
    data = Auto_notification.objects.filter(uname=name, status="Not Approved")
    return render(request, "auto/notifications.html", {'noti': data})


# --------------------------------------------------
#  approve  button on notification page
# --------------------------------------------------


def approve_delivery(request, id):
    uname = request.session['username']
    n = Auto_reg.objects.get(Username=uname)
    name = n.Name
    Auto_notification.objects.filter(id=id, uname=name, status="Not Approved").update(status="Approved")
    return redirect('autoapp/load_notifications')


# --------------------------------------------------
#  load delivery status page
# --------------------------------------------------


def load_delivery_status(request):
    uname = request.session['username']
    n = Auto_reg.objects.get(Username=uname)
    name = n.Name
    data = Auto_notification.objects.filter(uname=name, status="Approved")
    return render(request, "auto/delivery_status.html", {'noti': data})


# --------------------------------------------------
#  update delivery on delivery status page
# --------------------------------------------------

def update_delivery(request, id):
    uname = request.session['username']
    n = Auto_reg.objects.get(Username=uname)
    name = n.Name
    d = Auto_notification.objects.get(id=id, uname=name, status="Approved")
    it = d.items
    st = d.status
    p = Purchase.objects.get(Autoname=name, Status="Pending")
    i = p.items
    if it == i and st == "Approved":
        Purchase.objects.filter(Autoname=name, items=it, Status="Pending").update(Status="Delivered")
        Auto_notification.objects.filter(id=id, uname=name, status="Approved").update(status="Delivered")
    return redirect('/autoapp/load_delivery_status')




# --------------------------------------------------
#  load auto_book page
# --------------------------------------------------


def load_auto_book(request):
    uname = request.session['username']
    n = Auto_reg.objects.get(Username=uname)
    name = n.Name
    data = Auto_booking.objects.filter(Aname=name, Status="Requested")
    return render(request, "auto/auto_book.html", {'book': data})




# --------------------------------------------------
#  load auto_book page
# --------------------------------------------------


def approve_auto_book(request,id):
    uname = request.session['username']
    n = Auto_reg.objects.get(Username=uname)
    name = n.Name
    Auto_booking.objects.filter(id=id,Aname=name, Status="Requested").update(Status="Accepted")
    return render(request, "auto/index.html")






# --------------------------------------------------
# clearing the session id of user by logging out
# --------------------------------------------------

def a_logout(request):
    del request.session['userid']
    del request.session['username']
    return render(request, "login/Login.html")
