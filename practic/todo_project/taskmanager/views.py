from django.shortcuts import render,redirect
from taskmanager.models import*
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.hashers import check_password

# Create your views here.
@login_required
def home(r):
    return render(r,'home.html')

def signup(r):
    if r.method=="POST":
        Userame=r.POST.get('Userame')
        Full_Name=r.POST.get('Full_Name')
        Email=r.POST.get('Email')
        usertype=r.POST.get('usertype')
        Password=r.POST.get('Password')
        Confirm_Password=r.POST.get('Confirm_Password')

        if Confirm_Password == Password:
            AuthUserModel.objects.create_user(
                username=Userame,
                full_name=Full_Name,
                email=Email,
                user_type=usertype,
                password=Confirm_Password
            )
            return redirect("signin")
    return render (r,"signup.html")

def signin(r):
    if r.method=="POST":
        Username=r.POST.get('Username')
        Password=r.POST.get('Password')

        user=authenticate(username=Username,password=Password)
        if user:
            login(r,user)
            messages.success(r,'successfully login')
            return redirect ("home")
        else:
            messages.warning(r,'invalid')
            return redirect('signin')
    return render (r,"signin.html")

def signout(r):
    logout(r)
    return redirect("signin")

@login_required
def chengepass(r):
    current_user=r.user
    if r.method=="POST":
        Current_Password=r.POST.get('old_password')
        new_password=r.POST.get('new_password')
        confirm_password=r.POST.get('confirm_password')

        if check_password(Current_Password,current_user.password):
            if new_password==confirm_password:
                current_user.set_password(new_password)
                current_user.save()
                return redirect('home')
    return render(r,"chengepass.html")