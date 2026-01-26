from django.shortcuts import render,redirect
from myapp.models import*
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib.auth import update_session_auth_hash
# Create your views here.

def home(r):
    return render(r,'home.html')

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        user_type=request.POST.get('user_type')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            UserModel.objects.create_user(
                username = username,
                email =email,
                user_type=user_type,
                password = confirm_password,
            )
            
            return redirect('signin')
    return render(request,'signup.html')

def signin(request):
    if request.method=="POST":
        Username=request.POST.get("Username")
        Password=request.POST.get("Password")
        print(Username)

        user=authenticate(request,username=Username,password=Password)
        if user:
            login(request,user)
            return redirect('home')
    return render(request,'signin.html')
   

def signout(r):
    logout(r)
    return render (r,'signout.html')

def dep_list(r):
    d_data=DepartModel.objects.all()

    context={
        'data':d_data
    }
    return render (r,'deplist.html')

def dep_Add(r):
    if r.method=="POST":
        departname=r.POST.get('departname')
        description=r.POST.get('description')

        DepartModel.objects.create(
        departname=departname,
        description=description,
    )
        return redirect("dep_list")
    return render (r,'depAdd.html')

def dep_Edit(r):
    E_data=DepartModel.objects.get(id=id)
    if r.method=="POST":
        departname=r.POST.get('departname')
        description=r.POST.get('description')

        E_data.departname=departname
        E_data.description=description
        E_data.save()
        return redirect('dep_list')
    context={
        'data':E_data
    }
    return render (r,'depEdit.html')

def dep_Delete(r):
    DepartModel.objects.get(id=id).delete()
    return redirect (r,'dep_list')
