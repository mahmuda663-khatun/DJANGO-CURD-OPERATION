from django.shortcuts import render ,redirect

from myapp.models import studentModel

# nicher function er maddhome amra sobgulo data add korlam
def studentAdd(request):
    student_data=studentModel.objects.all()  #   sob gulo data ke neyar jonno all() user kori
    context={
        'student_info':student_data
    }
    return render(request,'student.html',context)

def studentDelete(request,id): 
    studentModel.objects.get(id=id).delete() #   get(id=id) er mani holo amra data gulor akta akta id dhore tader delete korbo
    return redirect('studentAdd') # redirect mani ami delete korar por jei page chole jaite chai