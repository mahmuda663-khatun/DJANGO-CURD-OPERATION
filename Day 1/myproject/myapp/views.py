from django.shortcuts import render

# Create your views here.
def studentAdd(request):
    student_data=studentModel.object.all()
    context={
        'student_info':student_data
    }
    return render(request,'student.html',context)

def studentDelete(request,id):
    studentModel.object.get(id=id).delete()
    return redirect('studentAdd')