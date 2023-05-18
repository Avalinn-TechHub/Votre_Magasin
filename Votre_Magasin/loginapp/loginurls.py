from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginhome, name='loginhome'),
    path('l_about',views.l_about,name='l_about'),
    path('l_contact',views.l_contact,name='l_contact'),
    path('shophome',views.shophome,name='shophome'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('shopregistration',views.shopregistration,name='shopregistration'),
    path('insert_shop_reg/',views.insert_shop_reg,name='insert_shop_reg'),
    path('autoregistration', views.autoregistration, name='autoregistration'),
    path('insert_auto_reg/',views.insert_auto_reg,name='insert_auto_reg'),
    path('customer_registration',views.customer_registration,name='customer_registration'),
    path('insert_customer_reg',views.insert_customer_reg,name='insert_customer_reg'),
    path('checklogin/',views.checklogin,name='checklogin'),
]