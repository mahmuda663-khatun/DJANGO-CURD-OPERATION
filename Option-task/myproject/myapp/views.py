from django.shortcuts import render
from myapp.models import*
# Create your views here.

def productlist(r):
    pending=projectModel.objects.filter(status='pending')
    ongoing=projectModel.objects.filter(status='ongoing')
    completed=projectModel.objects.filter(status='completed')
    
    p_data=r.GET.get('status')
    print(p_data)
    if p_data:
        selected_data=projectModel.objects.filter(status=p_data)
    else:
        selected_data=projectModel.objects.all()
    context={
        'pending':pending,
        'ongoing':ongoing,
        'completed':completed,
        'selected_data': selected_data,
        'p_data':p_data, 
    }
    return render(r,'productlist.html',context)