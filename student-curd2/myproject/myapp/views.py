from django.shortcuts import render,redirect
from myapp.models import*
# Create your views here.
def home(r):

    return render(r,'home.html')

def student_list(r):
    student_data=studentModel.objects.all()

    context={
        'student':student_data
    }
    return render (r,'studentList.html',context)

def student_add(r):
    if r.method=="POST":
        s_Name=r.POST.get('Name')
        s_Roll=r.POST.get('Roll')
        s_Address=r.POST.get('Address')
        s_Date=r.POST.get('Date')
        s_Image=r.FILES.get('Image')
        studentModel.objects.create(
           Name= s_Name,
           Roll=s_Roll,
           Address=s_Address,
           Date=s_Date,
           Image=s_Image
        )
        return redirect('student_list')
    return render (r,'studentAdd.html')

def student_update(r,id):
    student_add=studentModel.objects.get(id=id)
    if r.method=="POST":
        id=id,
        s_Name=r.POST.get('Name')
        s_Roll=r.POST.get('Roll')
        s_Address=r.POST.get('Address')
        s_Date=r.POST.get('Date')
        s_Image=r.FILES.get('Image')

        student_add.Name= s_Name
        student_add.Roll=s_Roll
        student_add.Address=s_Address
        student_add.Date=s_Date
        if s_Image:
            student_add.Image=s_Image

        student_add.save()
        return redirect('student_list')
    contest={
        'student':student_add
    }
    return render(r,'studentUpdate.html',contest)

def student_delete(r,id):
    studentModel.objects.get(id=id).delete()
    return redirect('student_list')