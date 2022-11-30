from django.shortcuts import render, redirect
from django.contrib import messages
from pyexpat.errors import messages

from django.http import *
from .authenticate import Authenticate
from .models import User, Admin, Subcriber, MyModel, Prod
from .forms import *
from django.contrib.auth.models import auth


# Create your views here.
def index(request):
    form = UserForm()
    return render(request, 'index.html', {'form': form})

def index2(request):
    return render(request, 'index2.html')

def puma(request):
    return render(request, 'puma.html')


def about(request):
    return render(request, 'about.html')


def nike(request):
    return render(request, 'nike.html')

def adidas(request):
    return render(request, 'adidas.html')

def adminlogin(request):
    return render(request, 'adminlogin.html')

def login(request):
    return render(request, 'login.html')

def cart(request):
    return render(request,'cart.html')

def payment(request):
    return render(request, 'payment.html')


def userentry(request):
    users = User.objects.all()
    return render(request, "entry.html", {'users': users})


def userdetail(request):
    users = User.objects.all()
    return render(request, "userdetail.html", {'users': users})





def admintable(request):
    adminuser = Admin.objects.all()
    return render(request, 'admintable.html', {'adminusers': adminuser})


def create(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        form.save()
        redirect('/entry')
    form = UserForm()
    return render(request, 'create.html', {'form': form})





def adminentry(request):
    request.session['email'] = request.POST['email']
    request.session['password'] = request.POST['password']
    return redirect('/admintable')


def loginvalid(request):
    request.session['email'] = request.POST['email']
    request.session['password'] = request.POST['password']
    return redirect('/index2')

def edit(request, id):
    user = User.objects.get(user_id=id)
    return render(request, 'edit.html', {'user': user})


def update(request, id):
    user = User.objects.get(user_id=id)
    form = UserForm(request.POST, instance=user)
    form.save()
    return redirect('/userdetail')


def delete(request, id):
    user = User.objects.get(user_id=id)
    user.delete()
    return redirect('/userdetail')


def admindelete(request, adminid):
    adminuser = Admin.objects.get(id=adminid)
    adminuser.delete()
    return redirect('/admintable')


def create1(request):
    if request.method == "POST":
        form = AdminForm(request.POST)
        form.save()
        redirect('/admintable')
    form = AdminForm()
    return render(request, 'create1.html', {'form': form})


def edit1(request, adminid):
    user = Admin.objects.get(id=adminid)
    return render(request, 'edit1.html', {'user': user})


def update1(request, adminid):
    admin = Admin.objects.get(id=adminid)
    form = AdminForm(request.POST, instance=admin)
    form.save()
    return redirect('/')

def subcriber(request):
    subcribers = MyModel.objects.all()
    return render(request, "subcriber.html", {'subcriber': subcribers})

def my_form(request):
  if request.method == "POST":
    form = MyForm(request.POST)
    if form.is_valid():
      form.save()
  else:
      form = MyForm()
  return render(request, 'cv-form.html', {'form': form})



def Prodi(request):
    if request.method == 'GET':
        form = addprodform
        return render(request, 'addPro.html', {'form': form})
    else:
        form = addprodform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added Successfully.')
            return redirect('/admin/addPro')
        else:
            messages.error(request, 'Error!!.')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


    

def show(request):
    produ = Prod.objects.all()
    context = {
        'prod' : produ,
    }
    return render(request, 'shoes.html', context)


def cartt(request,id):
    Pro= Prod.objects.get(id=id)
    context = {
        'prod': Pro,
    }
    return render(request, 'cart1.html', context)
