
# Create your views here.

from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from . import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
import pandas as pd
import pickle 
import locale
data=pd.pandas.read_csv('/home/shreyank/miniproject/mini/home/static/img/excel/Cleaned_data.csv')
pipe=pickle.load(open("/home/shreyank/miniproject/mini/home/RidgeModel.pkl","rb"))

areaname=""
bathroom=""
gbhk=""
ganswer=""

def homepage(request):
    return render(request, "index.html")

# def answer(request):
#     return render(request,'answer.html',{'arae':areaname},{'bt':bathroom},{'bhk':gbhk},{'answer':ganswer})

def register(request):
    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')

def product(request):
    locations=sorted(data['location'].unique())
    dic={'name':'GUEST1','password':'GUEST','locations':locations}
    if request.method=='POST':
        aname=request.POST.get('location',False)
        areaname=aname
        bh=request.POST.get('bhk',False)
        gbhk=bh
        size=request.POST.get('size',False)
        bt=request.POST.get('bt',False)
        bathroom=bt
        print(aname,bh,size,bt)
        input=pd.DataFrame([[aname,size,bt,bh]],columns=['location','total_sqft','bath','bhk'])
        answer=(round((pipe.predict(input)[0]*100000),3))
        locale.setlocale(locale.LC_MONETARY, 'en_IN')
        answer=locale.currency(answer, grouping=True)
        ganswer=answer
        dict={'area':aname,'size':size,'bt':bt,'bhk':bh,'answer':answer}
        return render(request,'answer.html',{'dict':dict})
        
    return render(request,"product.html",dic)

def signup(request):
    username = request.POST['uname']
    uemail = request.POST['email']
    password0 = request.POST['password']
    password1 = request.POST['password1']
    if request.method == 'POST':
        myuser = User.objects.create_user(username,uemail,password0)
        myuser.save()
        return redirect('home')



def hlogin(request):
    if request.method=="POST":
        lemail=request.POST['loginemail']
        lpassword=request.POST['loginpass']
        user=authenticate(email=lemail,password=lpassword)
        if user is not None:
            login(request,user)
            messages.success(request,"sucess")
            return render(request,'home')
        else:
            messages.error(request,"invalid")
            return render(request,'home')

def hlogout(request):
    pass