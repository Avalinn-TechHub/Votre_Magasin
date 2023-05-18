from django.urls import path
from . import views

urlpatterns = [
    path('', views.ahome, name='ahome'),
    path('aabout/', views.aabout, name='aabout'),
    path('acontact/', views.acontact, name='acontact'),
    path('load_notifications/', views.load_notifications, name='load_notifications'),
    path('approve_delivery/<int:id>', views.approve_delivery, name='approve_delivery'),
    path('load_delivery_status',views.load_delivery_status,name='load_delivery_status'),
    path('update_delivery/<int:id>',views.update_delivery,name='update_delivery'),
    path('load_status',views.load_status,name='load_status'),
    path('update_status',views.update_status,name='update_status'),
    path('load_auto_book/',views.load_auto_book,name='load_auto_book'),
    path('approve_auto_book/<int:id>',views.approve_auto_book,name='approve_auto_book'),
    path('a_logout',views.a_logout,name='a_logout'),
    ]