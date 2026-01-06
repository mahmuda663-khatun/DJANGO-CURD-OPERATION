from django.shortcuts import render
from myapp.models import*
# Create your views here.

def studentlist(request):
    student_data=studentModel.objects.all() 

    context={
        'student_list': student_data
    }
    return render(request,'studentlist.html',context)

def base(request):

    return render(request,'base.html',)