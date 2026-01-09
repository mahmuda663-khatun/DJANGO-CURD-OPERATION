from django.shortcuts import render, redirect
from myapp.models import*
# Create your views here.
def home(req):
    return render(req,'home.html')

def teacherList(req):
    list=teacherModel.objects.all()
    context={
        'teacher':list
    }
    return render(req,'teacherList.html',context )

def teacherADD(req):
    if req.method=="POST":
        t_name=req.POST.get('Name')
        t_department=req.POST.get('Departmentme')
        t_email=req.POST.get('Email')
        t_joininjdate=req.POST.get('Joininjdate')
        t_salay=req.POST.get('Salay')
        t_pic=req.FILES.get('Pic')

        teacherModel.objects.create(
            name=t_name,
            department=t_department,
            email=t_email,
            joininjdate=t_joininjdate,
            salay=t_salay,
            picture=t_pic,
        )
        return redirect('teacherList')
    return render(req,'teacherADD.html')

def teacherDelete(req,id):
    teacherModel.objects.get(id=id).delete()
    return redirect('teacherList')

def teacherUpdate(req,id):
    t_teacher=teacherModel.objects.get(id=id)
    if req.method=="POST":
        t_name=req.POST.get('Name')
        t_department=req.POST.get('Departmentme')
        t_email=req.POST.get('Email')
        t_joininjdate=req.POST.get('Joininjdate')
        t_salay=req.POST.get('Salay')

        teacherModel(
            id=id,
            name=t_name,
            department=t_department,
            email=t_email,
            joininjdate=t_joininjdate,
            salay=t_salay,
        ).save()
        return redirect('teacherList')
    context={
        'teacher':t_teacher
    }
    return render (req,'teacherUpdte.html',context)