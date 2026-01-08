from django.shortcuts  import render, redirect
from myapp.models import*
# Create your views here.

def home(r):
    return render (r,'home.html')

def saleryList(r):
    salary_data=salaryModel.objects.all()

    context={
        'salary':salary_data
    }
    return render(r,'Listsalary.html',context)

def salaryADD(r):
    if r.method=="POST":
        tmibonusdaw=int(r.POST.get('Bouns'))
        tmrsalarybolo=int(r.POST.get('Basic_salary'))
        overkoto=int(r.POST.get('overtime_hours'))
        ta_parcentkoto=float(r.POST.get('ta_percent'))
        da_persentkoto=float(r.POST.get('da_percent'))
        hr_persentkorto=float(r.POST.get('her_percent'))
        s_pic=r.FILES.get('Picture')

        Hra=(hr_persentkorto/100)*tmrsalarybolo
        DA=(da_persentkoto/100)*tmrsalarybolo
        TA=(ta_parcentkoto/100)*tmrsalarybolo
        overtime=overkoto*100

        gross=int(tmrsalarybolo+Hra+TA+DA+tmibonusdaw+overtime)

        salaryModel.objects.create(
                Bouns=tmibonusdaw,
                Basic_salary=tmrsalarybolo,
                overtime_hours=overtime,
                ta_percent=TA,
                da_percent=DA,
                her_percent=Hra,
                Gross_salary=gross,
                Picture=s_pic,
             )
        return redirect('saleryList')   
    return render (r,'Addsalary.html')

def salaryDelete(r,id):
    salaryModel.objects.get(id=id).delete()
    return redirect('saleryList')

def salaryUpdate(r,id):
    salary=salaryModel.objects.get(id=id)
    if r.method=="POST":
        tmibonusdaw=int(r.POST.get('Bouns'))
        tmrsalarybolo=int(r.POST.get('Basic_salary'))
        overkoto=int(r.POST.get('overtime_hours'))
        ta_parcentkoto=float(r.POST.get('ta_percent'))
        da_persentkoto=float(r.POST.get('da_percent'))
        hr_persentkorto=float(r.POST.get('her_percent'))
        s_pic=r.FILES.get('Picture')

        Hra=(hr_persentkorto/100)*tmrsalarybolo
        DA=(da_persentkoto/100)*tmrsalarybolo
        TA=(ta_parcentkoto/100)*tmrsalarybolo
        overtime=overkoto*100

        gross=int(tmrsalarybolo+Hra+TA+DA+tmibonusdaw+overtime)

        salaryModel(
                id=id,
                Bouns=tmibonusdaw,
                Basic_salary=tmrsalarybolo,
                overtime_hours=overtime,
                ta_percent=TA,
                da_percent=DA,
                her_percent=Hra,
                Gross_salary=gross,
                Picture=s_pic,
             ).save()
        
        return redirect('saleryList')
    context={
        'S_salary':salary
    }
    return render(r,'Updatesalary.html',context)