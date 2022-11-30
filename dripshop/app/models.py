from django.db import models


class User(models.Model):
    user_id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = "userinfo"


class Subcriber(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    subemail = models.CharField(max_length=100)

    class Meta:
        db_table = "subscriber"


class Admin(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    adminname = models.CharField(max_length=100)
    adminemail = models.CharField(max_length=100)
    adminpassword = models.CharField(max_length=100)

    class Meta:
        db_table = "adminuser"




 
class MyModel(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)



class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    price = models.IntegerField(max_length=50)
    image_url = models.CharField(max_length=2000)
    created_Date = models.DateTimeField(auto_now_add=True)


class Prod(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    price = models.CharField(max_length=50)
    pic = models.FileField(upload_to='static/uploads', null=True)
