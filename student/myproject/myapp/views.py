from django.shortcuts import render
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
    return render(r)

def studentUpdate(r):
    return render(r)

def studentDelete(r):
    return render(r)