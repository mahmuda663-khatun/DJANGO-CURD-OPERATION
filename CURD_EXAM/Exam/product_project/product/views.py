from django.shortcuts import render,redirect
from product.models import* 
# Create your views here.
def home(r):
    return render(r,'home.html')

def productList(r):
    product_data=ProductModel.objects.all()

    context={
    'product':product_data
    }
    return render(r,'productList.html',context)

def productAdd(r):
    if r.method=="POST":
       p_name=r.POST.get('name') 
       p_description=r.POST.get('description') 
       p_price=r.POST.get('price') 
       p_date=r.POST.get('date') 
       p_image=r.FILES.get('image') 

       ProductModel.objects.create(
           name=p_name,
           description=p_description,
           price=p_price,
           date=p_date,
           image=p_image
       )
       return redirect('productList')
    return render(r,'productAdd.html')

def productUpdate(r,id):
    product=ProductModel.objects.get(id=id)
    if r.method=="POST":
       id=id
       p_name=r.POST.get('name') 
       p_description=r.POST.get('description') 
       p_price=r.POST.get('price') 
       p_date=r.POST.get('date') 
       p_image=r.FILES.get('image') 
        
       product.name=p_name
       product.description=p_description
       product.price=p_price
       product.date=p_date
       if p_image:
        product.image=p_image
       product.save()
       return redirect('productList')
    context={
        'products':product
    }
    return render(r,'productUpdate.html',context)

def productDelete(r,id):
    ProductModel.objects.get(id=id).delete()
    return redirect('productList')