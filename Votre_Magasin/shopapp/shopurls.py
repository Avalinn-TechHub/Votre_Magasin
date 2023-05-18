from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.shophome, name='shophome'),
                  path('shoperror/', views.shoperror, name='shoperror'),
                  path('shopcontact', views.shopcontact, name='shopcontact'),
                  path('shopabout', views.shopabout, name='shopabout'),
                  path('logout/', views.logout, name='logout'),
                  path('load_addproduct/', views.load_addproduct, name='load_addproduct'),
                  path('insert_addproduct/', views.insert_addproduct, name='insert_addproduct'),
                  path('viewproducts/',views.viewproducts,name='viewproducts'),
                  path('viewprofile/', views.viewprofile, name='viewprofile'),
                  path('update_profile/', views.update_profile, name='update_profile'),
                  path('load_update_product/<int:id>',views.load_update_product,name='load_update_product'),
                  path('update_product/<int:id>',views.update_product,name='update_product'),
                  path('load_orders/',views.load_orders,name='load_orders'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
