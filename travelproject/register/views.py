from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        userna=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=userna,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid User")
            return redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name = request.POST['firstname']
        second_name = request.POST['secondname']
        email = request.POST['email']
        phone = request.POST['phonenumber']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already existing')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already existing')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=second_name,email=email,password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request,'Password not matching')
            return redirect('register')
        print('registration successful')
        return redirect('/')
    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')