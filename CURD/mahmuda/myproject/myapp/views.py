from django.shortcuts import render,redirect
from myapp.models import*
# Create your views here.

def base(r):
    return render(r,'base.html')

def calculate_grade(mark):
    if mark>=80:
        return 'A+'
    
    elif mark>=70 and mark<=79:
        return 'A'
    
    else:
        return 'fail'

def productlist(r):
    product=productModel.objects.all()
    context={
        'student':product
    }
    return render(r,'productlist.html', context)

def productADD(r):
    if r.method=="POST":
        p_name=r.POST.get('name') 
        p_description=r.POST.get('description') 
        p_price=r.POST.get('Price') 
        p_created_at=r.POST.get('created_at') 
        p_mark=int(r.POST.get('mark'))

        grade=calculate_grade(p_mark)

        productModel.objects.create (
            name=p_name,
            description=p_description,
            price=p_price,
            created_at=p_created_at,
            grade=grade,
        )
        return redirect('productlist')
    return render(r,'productADD.html')


def productDelete(r,id):
    productModel.objects.get(id=id).delete()
    return redirect('productlist')


def editproduct(r,id):
    stude_id=productModel.objects.get(id=id)
    if r.method=="POST":
        p_name=r.POST.get('name') 
        p_description=r.POST.get('description') 
        p_price=r.POST.get('Price') 
        p_created_at=r.POST.get('created_at') 
        p_mark=int(r.POST.get('mark'))

        grade=calculate_grade(p_mark)

        productModel(
            id=id,
            name=p_name,
            description=p_description,
            price=p_price,
            created_at=p_created_at,
            grade=grade,
        ).save()
        return redirect('productlist')
    context={
        'student':stude_id
    }
    return render(r,'edit.html',context)

# salary page 
def HAR (hra_percent,basic_salary):
    hra=(hra_percent/100)*basic_salary
    return hra
    # return render()

def DR (da_percent,basic_salary):
    pass
    # return render()

def TA (ta_persent,basic_salary):
    pass
    # return render()

def Over_time (overtime_hours):
    pass
    # return render()

def Gross_Salary(basic_salary,hra,TA,DA,bouns,overtime):
    gasalary=basic_salary+HAR+DR+TA
    # return render() 