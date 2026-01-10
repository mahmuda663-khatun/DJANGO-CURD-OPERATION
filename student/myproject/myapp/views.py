from django.shortcuts import render ,redirect
from myapp.models import*
# Create your views here.
def home(r):
    return render(r,'home.html')

def studentList(r):
    student_data=studentModel.objects.all()
    context={
        'student':student_data
    }
    return render(r,'studentList.html', context)

def studentADD(r):
    if r.method=="POST":
       s_Name=r.POST.get('Name')
       s_Course=r.POST.get('Course')
       s_Total_Marks=r.POST.get('Total_Marks')
       s_image=r.FILES.get('image')

       studentModel.objects.create(
           Name=s_Name,
           Course=s_Course,
           Total_Marks=s_Total_Marks,
           image=s_image,
       )
       return redirect('studentList')
    return render(r,'studentADD.html')

def studentUpdate(r,id):
    student=studentModel.objects.get(id=id)
    if r.method=="POST":
       s_Name=r.POST.get('Name')
       s_Course=r.POST.get('Course')
       s_Total_Marks=r.POST.get('Total_Marks')
       s_image=r.FILES.get('image')

       student.Name = s_Name
       student.Course = s_Course
       student.Total_Marks = s_Total_Marks

       if s_image:
         student.image = s_image

         student.save()

    #    studentModel(
    #        id=id,
    #        Name=s_Name,
    #        Course=s_Course,
    #        Total_Marks=s_Total_Marks,
    #        image=s_image,
    #    ).save()
       return redirect('studentList')
    context={
        'student':student
    }
    return render (r,'studentUpdate.html', context)

def studentDelete(r,id):
    studentModel.objects.get(id=id).delete()
    return redirect('studentList')