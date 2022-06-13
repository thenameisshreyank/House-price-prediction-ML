
from distutils.log import error

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import pandas as pd
import pickle 
from django.contrib import messages

data=pd.pandas.read_csv('/home/shreyank/miniproject/mini/home/static/img/excel/Cleaned_data.csv')


# Create your views here.

def signup(request):
    if request.method=='POST':
        uname=request.POST['uname']
        emailid=request.POST['email']
        password1=request.POST['password']
        password2=request.POST['password1']
        if password1!=password2:
            print("not matching")
        else:
            x=User.objects.create_user(username=uname,email=emailid,password=password1)
            x.save()
    return render(request,"register.html")

def login(request):
    locations=sorted(data['location'].unique())
    if request.method=='POST':
        uname=request.POST.get('lname')
        lpassword=request.POST.get('loginpass')
        user = authenticate(username=uname, password=lpassword)
        #dic={'name':uname,'password':lpassword,'locations':locations}
        if user is not None:
            messages.success(request,"LOGIN SUCESS!")
            return render(request,'product.html',{'name':uname,'password':lpassword})
        else:
            messages.error(request,"INVALID USERNAME OR PASSWORD")
            print(" no sucesss")
    return render(request,'login.html')


def details(request):
    
    return render(request,'details.html')

    
