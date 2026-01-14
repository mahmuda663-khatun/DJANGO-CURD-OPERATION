from django.shortcuts import render, redirect
from myapp.models import*
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required
def home(r):
    return render(r,"home.html")

def signUp(r):
    if r.method=="POST":
        username=r.POST.get('username')
        full_name=r.POST.get('full_name')
        email=r.POST.get('email')
        confirm_password=r.POST.get('confirm_password')
        password=r.POST.get('password')

        user_exists=customUser.objects.filter(username=username).exists()

        if user_exists:
            messages.warning(r,'username already exists')
            return redirect('signin')

        if password==confirm_password:
            customUser.objects.create_user(
                username=username,
                full_name=full_name,
                email=email,
                password=confirm_password,
            )
            return redirect('signin')
    return render(r,"signUp.html")

def signin(r):
    if r.method=="POST":
        username=r.POST.get('username')
        password=r.POST.get('password')
        print(username)
        user=authenticate(r,username=username,password=password)
        if user:
            login(r,user)
            messages.success(r,'successfully login') 
        else:
            messages.warning(r,'invalid')
        
        return redirect('home')
    return render(r,"signin.html")

def signOut(r):
    logout(r)
    return redirect('signin')