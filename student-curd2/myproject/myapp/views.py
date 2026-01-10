from django.shortcuts import render
from myapp.models import*
# Create your views here.
def home(r):

    return render(r,'home.html')

def student_list(r):
    
    return render (r)

def student_add(r):
    return render (r)

def student_update(r):
    return render(r)

def student_delete(r):
    return render(r)