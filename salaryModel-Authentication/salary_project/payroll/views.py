from django.shortcuts import render ,redirect
from payroll.models import*
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

@login_required
def home(r):
    return render(r,"home.html")

def signup(r):
    if r.method=="POST":
        username=r.POST.get('username')
        company_name=r.POST.get('company_name')
        email=r.POST.get('email')
        password=r.POST.get('password')
        confirm_password=r.POST.get('confirm_password')

        user_exits=AuthUserModel.objects.filter(username=username).exists()
        
        if user_exits:
            messages.warning("user already exits")
            return redirect('signin')

        if confirm_password==password:
          AuthUserModel.objects.create_user(
              username=username,
              company_name=company_name,
              email=email,
              password=confirm_password,
          ) 
          return redirect("signin") 
    return render(r,'signup.html')

def signin(r):
    if r.method=="POST":
        username=r.POST.get('username')
        password=r.POST.get('password')
        print(username)

        user=authenticate(r,username=username,password=password)
        if user:
           login(r,user) 
           messages.success(r,'successfully login')
           return redirect("home")
           
        else:
           messages.warning(r,'invalid')
           return redirect('signin')
        
    return render(r,"signin.html")

def salarylist(r):
    salary_data=SalaryModel.objects.all()

    context={
        'salary':salary_data
    }
    return render(r,'salarylist.html',context)


def addSalary(r):
    if r.method=="POST":
        empolyee_name=r.POST.get('empolyee_name'),
        employee_photo=r.FILES.get('employee_photo'),
        basic_salary=int(r.POST.get('basic_salary')),
        har=int(r.POST.get('har')),
        bonus=int(r.POST.get('bonus')),
        tax_percentage=float(r.POST.get('tax_percentage')),

        gross_salary=int(basic_salary+har+bonus)
        net_salary=int(gross_salary)-(int(gross_salary)*float(tax_percentage)/100)

        SalaryModel(
           empolyee_name=empolyee_name,
           employee_photo=employee_photo,
           basic_salary=basic_salary,
           har=har, 
           bonus=bonus,
           tax_percentage=tax_percentage,
           gross_salary=gross_salary,
           net_salary=net_salary,
        ).save()

        return redirect("salarylist")
    return render(r,'addSalary.html')