

from django.urls import path, include
from app import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name="index"),
    path('puma', views.puma, name="puma"),
    path('about', views.about, name="about"),
    path('nike', views.nike, name="nike"),
    path('adidas', views.adidas, name="adidas"),
    path('index2', views.index2, name="index2"),
    path('cart', views.cart, name="cart"),
    path('payment', views.payment, name="payment"),
    

    # CRUD
    path('create', views.create, name="create"),
    path('loginvalid', views.loginvalid, name="loginvalid"),
    path('login', views.login, name="login"),
    path('adminentry', views.adminentry, name="adminentry"),
    path('userentry', views.userentry),
    path('edit/<int:id>', views.edit, name="edit"),
    path('update/<int:id>', views.update, name="update"),
    path('delete/<int:id>', views.delete, name="delete"),
    #     admin
    path('admin', include('app.urls')),
    path('admindelete/<int:adminid>', views.admindelete),
    path('create1', views.create1),
    path('edit1/<int:adminid>', views.edit1),
    path('update1/<int:adminid>', views.update1),
    path('admin', views.adminlogin),
    path('userdetail', views.userdetail, name='userdetail'),
    path('admintable', views.admintable),
    path('adminlogin', views.adminlogin, name='adminlogin'),
    path('subcriber', views.subcriber),
    path('form', views.my_form, name='form'),
    path('/addPro', views.Prodi),
    path('shoes', views.show),
    path('cart1/<int:id>',views.cartt)
    
]
