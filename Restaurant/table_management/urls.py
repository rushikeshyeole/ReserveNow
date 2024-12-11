from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.index),
    path('wlC', views.wlc),
    path('Contact', views.contact),
    path('cor', views.COr),
    path('cus_Or', views.Cus_or),
    path('owner',views.Show_Cus_data),
    path('Cont_det', views.Cus_Contact_Us),
    path('Rooms', views.rooms),
    path('About', views.about_us),
    # path('Restaurant', views.restaurant),
    path('Thali_Items_save', views.thali_items_save),
    path('Todays_Thali_Items', views.thali_Items),
    path("Restaurant", views.thali_items_show),
    path('Thali_items_SO', views.thali_items_show_owner),
    path('Thali_items_delete', views.thali_items_delete),
    path('Box_co_ch', views.box_co_ch),
]
