from django.shortcuts import render,redirect
from jobportalapp.models import*
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(r):
    return render(r,'home.html')

def signup(r):
    if r. method=="POST":
      user_type=r.POST.get('user_type')  
      user_name=r.POST.get('user_name')  
      email=r.POST.get('email')  
      password=r.POST.get('password')  
      Confirm_Password=r.POST.get('Confirm_Password') 

      if Confirm_Password==password:
        userModel.objects.create_user(
            user_type=user_type, 
            username=user_name,
            email=email, 
            password=Confirm_Password,
        )
        return redirect("signin")  
    return render(r,'signup.html')

def signin(r):
    if r. method=="POST":  
      user_name=r.POST.get('user_name')  
      password=r.POST.get('password')
      user=authenticate(r,username=user_name,password=password)

      if user:
        login(r, user)
        return redirect("home") 
    return render (r,'signin.html')

def signout(r):
    logout(r)
    return redirect("signin")