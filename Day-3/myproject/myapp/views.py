from django.shortcuts import render, redirect
from myapp.models import *
# Create your views here.
def base(r):
    return render(r,'base.html')

def productlist(r):
    product_data = productModel.objects.all()

    context={
        'product': product_data
    } 
    return render(r,'productlist.html',context)
def productADD(r):
    if r.method=="POST":
        p_name = r.POST.get('name')
        p_description = r.POST.get('description')
        p_price = r.POST.get('price')
        p_date = r.POST.get('date')

        productModel.objects.create(
           name = p_name,
           description = p_description,
           price = p_price,
           date = p_date
        ) 
        return redirect('productlist')
    return render(r,'productADD.html')