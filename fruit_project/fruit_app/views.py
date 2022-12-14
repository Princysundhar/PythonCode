from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import fruit_shop
from .forms import FruitForm
# Create your views here.
def index(request):
    fruits=fruit_shop.objects.all()
    context={
        'fruits_list':fruits
    }
    return render(request,'index.html',context)

def detail(request,fruit_id):
    fruits=fruit_shop.objects.get(id=fruit_id)
    return render(request,'detail.html',{'fruit':fruits})

def add_fruit(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc = request.POST.get('desc')
        price = request.POST.get('price')
        image = request.FILES['image']

        fruits=fruit_shop(name=name,desc=desc,price=price,image=image)
        fruits.save()
    return render(request,'add_fruit.html')


def update(request,id):
    fruits=fruit_shop.objects.get(id=id)
    form=FruitForm(request.POST or None,request.FILES,instance=fruits)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'fruit':fruits})


def remove(request,id):
    if request.method=='POST':
        fruits=fruit_shop.objects.get(id=id)
        fruits.delete()
        return redirect('/')
    return render(request,'remove.html')