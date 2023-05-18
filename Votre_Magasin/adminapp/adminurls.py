from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='adminhome'),
    path('viewshop/', views.viewshop, name='viewshop'),
    path('approvestore/<int:id>', views.approvestore, name='approvestore'),
    path('load_approveform/<int:id>', views.load_approveform, name='load_approveform'),
    path('disapproveshop/<int:id>', views.disapproveshop, name='disapproveshop'),
    path('viewauto/', views.viewauto, name='viewauto'),
    path('approveauto/<int:id>', views.approveauto, name='approveauto'),
    path('load_approveauto/<int:id>', views.load_approveauto, name='load_approveauto'),
    path('disapproveauto/<int:id>', views.disapproveauto, name='disapproveauto'),
    path('404/', views.error, name='404'),
    path('admincontact', views.admincontact, name='admincontact'),
    path('adminabout', views.adminabout, name='adminabout'),
    path('category/', views.category, name='category'),
    path('addcategory/', views.addcategory, name='addcategory'),
    path('viewcategory/', views.viewcategory, name='viewcategory'),
    path('load_update_category/<int:id>', views.load_update_category, name='load_update_category'),
    path('update_category/<int:id>', views.update_category, name='update_category'),
    path('subcategory/', views.subcategory, name='subcategory'),
    path('addsubcategory', views.addsubcategory, name='addsubcategory'),
    path('viewsubcategory', views.viewsubcategory, name='viewsubcategory'),
    path('load_update_subcategory/<int:id>', views.load_update_subcategory, name='load_update_subcategory'),
    path('update_subcategory/<int:id>', views.update_subcategory, name='update_subcategory'),
    path('adlogout/', views.adlogout, name='adlogout'),
]
