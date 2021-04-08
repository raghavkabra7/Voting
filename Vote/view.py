from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import User_detail
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from .models import User_detail,Nominance,Party
def Home(request):
    data = Party.objects.all()
    d = {"party":data}
    return render(request,'index.html',d)

def Login(request):
    error = False
    if request.method == "POST":
         d = request.POST
         m = d['mob']
         p = d['password']
         user = authenticate(username = m,password = p)
         if user:
             login(request,user)
             if user.is_staff:
                 return redirect('admin')
             else:
                 return HttpResponse("You are Voter")
         else:
             error = True
    d = {"error": error}
    return render(request,'login.html',d)


def forgot(request):
    return render(request,'forgot.html')

def how(request):
    return render(request,'how.html')


def signup(request):
    error = False
    error2 = False
    if request.method == "POST":
         d = request.POST
         n = d['name']
         e = d['email']
         m = d['Mobail']
         a = d['aadhar']
         p = d['password']
         cp = d['confirmPassword']
         id = d['id_proof']
         dob = d['DOB']
         i = request.FILES['image']
         data = User.objects.filter(username = m)
         if data:
             error = True
         elif cp!=p:
             error2 = True
         else:

                 u = User.objects.create_user(username = m,password=p)
                 User_detail.objects.create(usr = u,name = n, email = e,mobile = m,aadhar = a,id_proof = id,photo = i,DOB = dob, )
    d = {"error":error,"error2":error2}
    return render(request,'register.html',d)


def Party_detail(request,pid):
    data = Party.objects.get(id = pid)
    d = {"party":data}
    return render(request,'Nominance.html',d)


