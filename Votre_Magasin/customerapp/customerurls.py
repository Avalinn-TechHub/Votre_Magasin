from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='chome'),
    path('cerror/', views.cerror, name='cerror'),
    path('c_contact/', views.c_contact, name='c_contact'),
    path('c_about/', views.c_about, name='c_about'),
    path('c_myprofile/', views.c_myprofile, name='c_myprofile'),
    path('c_view_products/', views.c_view_products, name='c_view_products'),
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/<int:id>',views.add_to_cart,name='add_to_cart'),
    path('edit_cart/<int:id>',views.edit_cart,name='edit_cart'),
    path('update_quantity/<int:id>',views.update_quantity,name='update_quantity'),
    path('delete_cart/<int:id>',views.delete_cart,name='delete_cart'),
    path('load_checkout',views.load_checkout,name='load_checkout'),
    path('place_order',views.place_order,name='place_order'),
    path('myorders/',views.myorders,name='myorders'),
    path('c_update_profile/', views.c_update_profile, name='c_update_profile'),
    path('load_auto_booking/',views.load_auto_booking,name='load_auto_booking'),
    path('book_auto/',views.book_auto,name='book_auto'),
    path('c_logout/', views.c_logout, name='c_logout'),
]
