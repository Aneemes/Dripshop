from django import forms
from .models import *


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"


class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = "__all__"


class loginform(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"


class adminloginform(forms.ModelForm):
    class Meta:
        model = Admin
        fields = "__all__"

class MyForm(forms.ModelForm):
  class Meta:
    model = MyModel
    fields = ["fullname", "email",]
    labels = {'fullname': "Name", "email": "Email",}

class ProductForm(forms.Form):
    class Meta:
        model = Product
        fields = ["name","description","price","image_url"]

class addprodform(forms.ModelForm):
    class Meta:
        model = Prod
        fields = "__all__"