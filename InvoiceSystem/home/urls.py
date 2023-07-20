from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path('',views.index,name="home"),
    path('invoice',views.invoice,name="invoice"),
    path('alluser_detail',views.alluser_detail,name="alluser_detail"),
    path('newbill',views.newbill,name="newbill"),
    path('userdetails/<str:pk>',views.userdetails,name="userdetails")
]