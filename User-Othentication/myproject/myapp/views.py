from django.shortcuts import redirect,render
from myapp.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required
def HomePage(request):
    return render(request,'home.html')


def SignUpPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        city = request.POST.get('city')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            customUser.objects.create_user(
                username = username,
                email =email,
                city = city,
                password = confirm_password,
            )
            
            return redirect('signin')
    return render(request,'signup.html')


def SignInPage(request):
    if request.method=="POST":
        Username=request.POST.get("Username")
        Password=request.POST.get("Password")
        print(Username)

        user=authenticate(request,username=Username,password=Password)
        if user:
            login(request,user)
            return redirect('home')
    return render(request,'signin.html')

def logoutPage(reguest):
    logout(reguest)
    return redirect("signin")